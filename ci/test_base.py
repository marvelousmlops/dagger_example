"""Execute a command."""

import os
import sys

import anyio
import dagger


async def test_and_publish():
    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        src = client.host().directory(".")
        source = (
            client.container()
            # pull container
            .from_("python:3.11-slim-bullseye")
            # mount source directory
            .with_directory("/ws", src)
        )
        # install package
        runner = (
            source.with_workdir("/ws")
            .with_exec(["pip", "install", "-r", "requirements.txt"])
            .with_exec(["pip", "install", ".[test]"])
        )

        # run tests
        test = runner.with_exec(["pytest", "-v", "tests"])

        # build python package
        py_build = (
            runner.with_exec(["python3", "-m", "pip", "install", "--upgrade", "build"])
            .with_exec(["python3", "-m", "build"])
            .directory("dist")
            .export("dist")
        )

        # build and publish image
        image_ref = "marvelousmlops/dagger_example:latest"
        secret = client.set_secret(
            name="dockerhub_secret", plaintext=os.environ["DOCKERHUB_TOKEN"]
        )
        build = (
            client.host()
            .directory(".")
            .docker_build()
            .with_registry_auth(
                address=f"https://docker.io/{image_ref}",
                secret=secret,
                username=os.environ["DOCKERHUB_USER"],
            )
        )
        await build.publish(f"{image_ref}")
    print(f"Published image to: {image_ref}")


if __name__ == "__main__":
    anyio.run(test_and_publish)

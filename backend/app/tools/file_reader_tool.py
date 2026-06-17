from app.logging import logger

from app.rag.document import Document


class FileReaderTool:

    @staticmethod
    def read_file(
        file_path: str
    ):

        try:

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:

                content = file.read()

            logger.info(
                f"Successfully read file: {file_path}"
            )

            return content

        except Exception as e:

            logger.error(
                f"Failed to read file: {file_path}"
            )

            return None

    @staticmethod
    def create_documents(
        file_paths: list[str]
    ):

        documents = []

        for file_path in file_paths:

            content = FileReaderTool.read_file(
                file_path
            )

            if not content:
                continue

            documents.append(
                Document(
                    content=content,
                    source=file_path
                )
            )

        logger.info(
            f"Created {len(documents)} documents"
        )

        return documents
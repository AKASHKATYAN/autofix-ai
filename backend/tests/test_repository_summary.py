from app.services.repository_summary_service import (
    RepositorySummaryService
)


def main():

    summary = (
        RepositorySummaryService.generate_summary(
            "repositories/langgraph"
        )
    )

    print()

    print(
        f"Repository: {summary.repository_name}"
    )

    print(
        f"Files: {summary.total_files}"
    )

    print(
        f"Languages: {summary.languages}"
    )

    print(
        "Directories:"
    )

    for directory in (
        summary.important_directories
    ):

        print(
            f"- {directory}"
        )


if __name__ == "__main__":

    main()
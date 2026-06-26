from app.services.architecture_service import (
    ArchitectureService
)

from app.services.repository_summary_service import (
    RepositorySummaryService
)


def main():

    summary = (
        RepositorySummaryService.generate_summary(
            "repositories/langgraph"
        )
    )

    architecture = (
        ArchitectureService.analyze(
            repo_path="repositories/langgraph",
            repository_summary=summary
        )
    )

    print()

    print(
        architecture.repository_name
    )

    print()

    print(
        architecture.architecture_summary
    )

    print()

    print("Modules:")

    for module in architecture.modules:

        print(
            f"- {module}"
        )


if __name__ == "__main__":

    main()
from app.services.repository_context_service import (
    RepositoryContextService
)


def main():

    context = (
        RepositoryContextService.generate(
            "repositories/langgraph"
        )
    )

    print()

    print(
        context.repository_summary.repository_name
    )

    print()

    print(
        context.repository_summary.frameworks
    )

    print()

    print(
        context.architecture.architecture_summary
    )


if __name__ == "__main__":

    main()
# Contribution Guidelines

## Coding

* <ins>**_NEVER CHECK IN CREDENTIALS!_**</ins>
* All code should be functional, readable, and easily maintainable.
   * Break any of the below guidelines if they are counter to this.
* Work requirements should be organized into a [backlog](/backlog).
* [Don't repeat yourself.](https://zapier.com/blog/dont-repeat-yourself/)
* Avoid [gold plating](https://en.wikipedia.org/wiki/Gold_plating_(project_management)).
* Don't follow bad practices for consistency.
* Prefer the "Easier to ask forgiveness than permission" ([EAFP](https://betterprogramming.pub/in-python-dont-look-before-you-leap-cff250881930)) over the "Look before you leap" (LBYL) coding style.
* Follow the [Principle of Least Astonishment](https://en.wikipedia.org/wiki/Principle_of_least_astonishment) (POLA)
* Whenever possible, be idempotent.
* [Almost never use global variables.](http://wiki.c2.com/?GlobalVariablesAreBad)
* All automation should execute as a user exclusively used for automation.
* All code dependencies must be accounted for either in an existing repo or within the SRE image.
* All programs should print their usage and exit if they are invoked with incorrect arguments.
* Programs should **always** clean up after themselves using try/finally or signal handling logic.

## Testing

* Focus on functional testing above all else.
* Do **NOT** create tests that check to see if an external tool or library ran correctly.
* Tests should be fast (under a minute, even shorter is better).

## Documentation

* Documentation should explain **what** code does.
   * All PRs must update the documentation associated with the changed code.
* Code should be [self-documenting](https://itnext.io/tips-for-writing-self-documenting-code-e54a15e9de2) to explain **how** it works.
* [Write good commit messages](https://chris.beams.io/posts/git-commit/) to explain **why** code does something.

## Pull Requests

* Your pull request title should explain what you're changing like a good git commit headline.
* Fill out all fields in the PR template before requesting a formal review.
* Code owners are responsible for reviewing PRs within two business days. Contact them if they do not.
* Rebase against origin/main before merging if your merge will create a conflict.
* When merging, always create a merge commit.
* Delete your branch from the remote repository after merging/closing a PR.
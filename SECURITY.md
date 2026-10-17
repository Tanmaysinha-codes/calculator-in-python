# Security Notes

## Repository audit summary

- Reviewed source, repository files, and available git history for committed credentials or private keys.
- No confirmed live secrets were found in tracked files in this repository state.
- No third-party runtime dependencies are currently defined for this project.

## Secret handling guidance

- Never commit `.env` files, private keys, or tokens.
- If a secret is ever discovered in git history, revoke/rotate it immediately. History rewrite is not applied automatically as part of routine fixes.

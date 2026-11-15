# Vendored code

`anthropic-sdk-1.3.0.mjs` is Anthropic's official JavaScript SDK (`@anthropic-ai/sdk` version 1.3.0), bundled into one browser file so the page doesn't load code from a CDN.

It includes these packages, whose licences are in `licenses/`:

| Package | Version | Licence |
|---|---|---|
| @anthropic-ai/sdk | 1.3.0 | Apache-2.0 |
| @opentelemetry/api | 1.10.0 | Apache-2.0 |
| @stablelib/base64 | 1.0.1 | MIT |
| fast-sha256 | 1.3.0 | Unlicense |
| standardwebhooks | 1.1.1 | MIT |

To rebuild or upgrade (change the version in both places, then update `SDK_URL` in `index.html`):

```sh
npm i @anthropic-ai/sdk@1.3.0
npx esbuild@0.24.0 node_modules/@anthropic-ai/sdk/index.mjs --bundle --format=esm --platform=browser --minify --legal-comments=eof --outfile=vendor/anthropic-sdk-1.3.0.mjs
```

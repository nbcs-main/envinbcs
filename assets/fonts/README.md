# Fonts

The site uses two free, open-licence fonts (SIL Open Font License 1.1: free for commercial use, no on-page credit needed):

- **Manrope** (headings) -> `manrope-latin-wght-normal.woff2`
- **Inter** (body text) -> `inter-latin-wght-normal.woff2`

Until these two files are in this folder the site falls back to the visitor's system font, so nothing breaks, it just does not look final.

## Easiest way to add them

1. Go to https://fontsource.org/fonts/manrope and https://fontsource.org/fonts/inter and use **Download** on each.
2. In the zip(s), copy the variable-font files `manrope-latin-wght-normal.woff2` and `inter-latin-wght-normal.woff2` into this folder.
3. Also copy each font's `LICENSE` file here and rename them `OFL-manrope.txt` / `OFL-inter.txt` (keeping the licence next to the files is the only obligation).

## Alternative (from the official TTF files)

```bash
pip install fonttools brotli
pyftsubset "Manrope[wght].ttf" --unicodes="U+0000-00FF,U+2013-2014,U+2018-201D,U+2022,U+2026,U+20B1" --flavor=woff2 --output-file=manrope-latin-wght-normal.woff2
pyftsubset "Inter[opsz,wght].ttf" --unicodes="U+0000-00FF,U+2013-2014,U+2018-201D,U+2022,U+2026,U+20B1" --flavor=woff2 --output-file=inter-latin-wght-normal.woff2
```
(`U+20B1` is the peso sign.)

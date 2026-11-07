# Comot branding fork of Concat

## Purpose
Preserve a self-hosted, locally usable development base independently of future upstream business decisions. This branch changes logo assets; it is not a new claim of authorship or a license exception.

## Repository layout
- `origin`: https://github.com/bettercalldull/Concat
- `upstream`: https://github.com/jub0t/Concat
- `main`: upstream-tracking branch, updated only by guarded fast-forward synchronization.
- `comot-branding`: Comot logo customization branch. Weekly synchronization MUST NOT reset, rebase, force-push or automatically merge this branch.
- `preserved-tested-v0.2.9`: preserved commit of the version exercised in Windows and isolated VPS evaluation.
- Local development clone: `C:/Users/asus/Projects/Concat-Comot`.
- VPS archive/controller: `/root/workspaces/concat-fork/`.

## Logo scope and provenance
The supplied brand is the existing Comot lime download-arrow mark. The canonical PNG was extracted unchanged from the local Comot header, saved as `tests/fixtures/comot-original.png` (128x128 RGBA). No download history, browser credentials, application settings or personal media are included.

Replaced: six desktop PNG icon sizes (16 through 512), Windows multi-size ICO, the 512px master/README mark, embedded UI logo, and four theme SVG containers. SVGs embed the original raster; they are not new vector artwork. Upscaled 512px assets cannot recover detail beyond the 128px original. The original Concat authoring file and historical screenshots are retained as upstream provenance, not presented as new Comot artwork.

Run `python scripts/comot-branding.py` to regenerate the assets. The developer utility and tests use Pillow, already available on the working laptop; no Hermes environment package was installed.

## Verification and build boundary
`python -m unittest discover -s tests -p test_comot_branding.py -v` verifies five test cases covering PNG pixels/sizes, ICO, SVG container payloads, embedded/README marks, and unchanged original legal notices.

This is a **source branding change**, not an installed replacement binary. The existing installed Concat0.2.9 has not been patched or replaced. A full editor build and UI/runtime verification of the branded binary remain pending; Rust/Cargo/CMake were not on the working laptopPATH, and no new toolchain installation was authorized.

## Upstream preservation and legal limits
Keep LICENSE,LICENSING.md,CLA.md,TRADEMARK.md and THIRD_PARTY_NOTICES.md intact. Upstream is AGPL-3.0-or-later and also offers a separate commercial license. Existing AGPL code remains usable subject to its terms; future proprietary releases or third-party models/components are not automatically covered. Network/distribution obligations require separate review for the actual use. This fork does not grant rights to upstream trademarks or waive codec-patent obligations.

The weekly VPS scheduler is maintained outside this repository; consult `/root/workspaces/concat-fork/setup-report.json` and `/root/workspaces/concat-fork/logs/latest.json` for actual installation/run status. It archives code and updates eligible forkmain commits, **not installed applications or clipper production**. License/legalnoticechanges,non-fast-forwardhistory or custommaincommits require manual review; customization branches remain untouched. Laptoppulls/merges into this branch are manual, not a promised always-on sync while the laptop is off.

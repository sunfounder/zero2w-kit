# SunFounder Zero 2W Starter Kit — Online Documentation

Source for the online manual of the **SunFounder Zero 2W Starter Kit** (P/N CN0552D),
written with [Sphinx](https://www.sphinx-doc.org/) and published on
[Read the Docs](https://readthedocs.org/).

**This branch contains the English documentation only.** English is the master copy.
Translations are maintained on separate branches — `docs-cn`, `docs-de`, `docs-es`,
`docs-fr`, `docs-it`, `docs-ja` — each created from this branch once the English text
has been reviewed and finalised. Do not add a second language to this branch.

## What the manual covers

Two kinds of page live in this repository, and the difference matters when you edit.

**Pages we own** (`docs/source/*.rst`) — kit-specific text:

| Page | Content |
| --- | --- |
| `index.rst` | About the kit, contents |
| `components.rst` | Full box-contents table (BOM), heatsink placement, fitting the case, what else you must supply |
| `set_up_pi.rst` | First boot: screen route, headless/SSH route, troubleshooting, graphical remote access |
| `appendix.rst` | Landing section for the shared VNC / SSH appendix pages |
| `faq.rst` | Hardware, boot, network and expansion FAQ |

`set_up_pi.rst` is **ours on purpose**. The shared version is written for every board, and
on a Zero 2 W that shows: it says the Pi "installed on the robot" is hard to connect to a
screen, tells you to use Ethernet (there is no Ethernet port), and its screen-setup photo
is a Raspberry Pi 5 with micro-HDMI and full-size USB. Owning the page lets it describe the
Mini HDMI adapter, the single USB data port and 2.4 GHz-only Wi-Fi instead.

**Shared pages** — written once for every SunFounder Raspberry Pi kit and maintained in
a separate repository, [`sunfounder/sf-shared`](https://github.com/sunfounder/sf-shared),
which is mounted at `docs/source/_shared` as a git submodule. Sphinx sees it as
`/_shared/...`:

| Page | Where it is listed |
| --- | --- |
| `_shared/pi_start/install_os_trixie.rst` | `index.rst` toctree, as "Installing the Operating System" |
| `_shared/appendix/remote_desktop.rst` | `appendix.rst` toctree |
| `_shared/appendix/install_openssh_powershell.rst` | `appendix.rst` toctree |
| `_shared/appendix/login_windows.rst` | `appendix.rst` toctree |

Local `set_up_pi.rst` still borrows two board-agnostic screenshots from the submodule
(`open_terminal.png`, `ssh_login.png`); those are OS screenshots, identical on every board.

The shared pages are referenced **directly** from the toctrees rather than wrapped in a
local file. That is deliberate: a wrapper that both includes a shared page and appears in
a toctree makes Sphinx parse the shared labels twice and emit duplicate-label warnings.
Reference them straight from the toctree instead, using an explicit title when the
generated heading is not what you want:

```rst
.. toctree::
    :maxdepth: 1

    Installing the Operating System <_shared/pi_start/install_os_trixie>
```

**Never paste shared text into this repository** — a fix belongs upstream so all kits get
it.

### Editing the shared pages

```bash
# make the change in a clone of sf-shared, open a PR there, then in this repo:
cd docs/source/_shared && git pull origin main && cd ../../..
git add docs/source/_shared      # records the new submodule commit
```

To move this docs tree to a newer shared revision, checkout the commit you want inside
`docs/source/_shared` and stage the result. Nothing else in this repo needs to change.

## Building locally

```bash
git clone --recurse-submodules <repo-url>
# or, in an existing clone:
git submodule update --init --recursive

python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r docs/requirements.txt

cd docs
make html
```

The HTML lands in `docs/build/html/`. Open `docs/build/html/index.html` in a browser.
On Windows use `make.bat html`.

`docs/source/conf.py` needs no environment variables and no configuration switching —
there is exactly one language on this branch.

### Verify in a clean clone before you push

A local build can pass while Read the Docs fails, and the usual cause is the submodule.
If `docs/source/_shared` was populated with a **sparse checkout** — for example because
the full clone kept timing out — files that a real clone has simply do not exist on your
disk, so Sphinx never sees them. `_shared/component` alone holds 55 pages this kit does
not use; they are excluded by directory in `conf.py` precisely because of this.

Once, before pushing a change that touches `conf.py` or `_shared`:

```bash
git clone --recurse-submodules <repo-url> /tmp/verify
cd /tmp/verify/docs && make html
```

It is the only check that reproduces the Read the Docs environment.

> **The submodule is not optional.** Without `docs/source/_shared` populated, the
> `install_os` page is empty, `appendix` has no pages, and `set_up_pi.rst` loses its two
> screenshots — the build fails on the missing includes.

## Repository layout

```
.
├── .github/workflows/docs.yml   # CI: builds the docs on every push
├── .readthedocs.yaml            # Read the Docs build configuration
├── .gitmodules                  # docs/source/_shared -> sunfounder/sf-shared
├── README.md
└── docs                         # the Sphinx project
    ├── Makefile / make.bat      # make html
    ├── requirements.txt
    └── source
        ├── conf.py              # Sphinx configuration
        ├── index.rst
        ├── components.rst   faq.rst
        ├── appendix.rst
        ├── img/                 # cover + packing list, from the retail card
        │   ├── kit-cover.png
        │   └── packing-list.png
        ├── _static/lang.js      # SunFounder: "also available in…" language hint
        ├── _templates/layout.html  # SunFounder: top navigation bar + <title>
        └── _shared/             # git submodule: sunfounder/sf-shared
            ├── pi_start/        # shared OS install + Pi setup guides
            └── appendix/        # shared VNC / SSH appendix pages
```

### SunFounder site customisation

Every SunFounder docs site carries the same chrome, and `conf.py` wires it up the
same way here:

| Piece | What it does |
| --- | --- |
| `html_css_files` → `https://ezblock.cc/readDocFile/custom.css` | SunFounder styling, hides the theme's own version/language selectors |
| `html_js_files` → `https://ezblock.cc/readDocFile/custom.js` | SunFounder top bar behaviour |
| `html_js_files` → `./lang.js` | `_static/lang.js`: offers a link to the translated version of the page if one exists for the visitor's browser language |
| `_templates/layout.html` | The SunFounder logo navigation bar, plus a `<title>` override so the home page does not repeat the project name |

Do not remove `templates_path` / `html_static_path` — Sphinx warns if a declared
path is missing, and the two files would silently drop out of the build.

**One deliberate difference from the other repos:** they also set
`flyout_display`, `version_selector` and `language_selector` in
`html_theme_options`. Those are **not** options of the published
`sphinx_rtd_theme` — Sphinx reports them as "unsupported theme option" and ignores
them. That goes unnoticed in the other repos because their builds do not use `-W`.
This one does, so the three are omitted; the visual effect comes from `custom.css`
either way.

## Repository

<https://github.com/sunfounder/zero2w-kit> — public, default branch `main`.

The documentation is **not on Read the Docs yet**; follow the next section to publish it.

## Publishing on Read the Docs

1. Sign in to <https://readthedocs.org/> and choose **Import a Project → Import
   Manually**.
2. Repository URL: `https://github.com/sunfounder/zero2w-kit`.
3. **Project slug**: `zero2w-kit` — this becomes the URL.
4. Set the default branch to `main` and enable **Build pull requests**.
5. Repeat for each translation branch when it exists, setting the project language
   accordingly.

Read the Docs reads `.readthedocs.yaml`, installs `docs/requirements.txt`, and builds
`docs/source/conf.py` with `docs/source/` as the source root. That is the standard
layout, so no build-job override is needed. `submodules: include: all` makes it fetch
`sf-shared` automatically — without that the shared pages come out empty.

After the first successful build, tighten `.readthedocs.yaml` by setting
`fail_on_warning: true` so that a broken reference fails the build instead of
silently shipping.

## Adding a translation branch

Do this only after the English text has been reviewed.

```bash
git switch -c docs-cn
# translate the .rst files in docs/source/ in place, keeping the file names
```

Keep the page file names identical to the English ones so that the Read the Docs
language switcher and any cross-references stay aligned. Drop the English-specific
`.. note::` at the top of each page only if the translation has its own equivalent.

## Notes for contributors

* **One language per branch.** Never add a translation to this branch; create a
  `docs-<lang>` branch instead.
* **Title underlines.** RST section underlines must be at least as long as the title.
* **Images.** Our own images live in `docs/source/img/` and are referenced relative to
  `docs/source/`, for example `.. image:: img/kit-cover.png`. Never reference a file that
  is not in the repository — Sphinx fails the build (and CI runs with `-W`).
  `make html` copies referenced images into the output automatically; no `html_static_path`
  entry is needed.
* **Never copy text out of `_shared/`.** If a shared page is wrong or incomplete, fix it in
  `sunfounder/sf-shared` and bump the submodule. Copying it here means every kit keeps its
  own divergent version.
* **Do not document Raspberry Pi OS features that Raspberry Pi documents itself.** Remote
  desktop and Raspberry Pi Connect are covered by the shared Appendix page and by
  Raspberry Pi's own documentation — link to those rather than writing our own version.
* **No video embeds.** This kit has no video tutorials, and `sphinxcontrib.youtube` is
  deliberately not enabled. If videos are ever produced, add the extension and the
  `.. youtube::` directive together, with `:aspect: 16:9` (not `:aspect_ratio:`).

## Known gaps / TODO

- [x] **Build the docs.** `sphinx-build -b html -W --keep-going` passes with **zero
      warnings** (`Sphinx 7.4.7`), so the markup, cross-references and images are clean.
- [x] **Cover and packing list are in place.** Both are rendered at 300 dpi from the
      retail card (`K0433V10-A0001442`) into `docs/source/img/`:
  - `img/kit-cover.png` — used on the `index` page
  - `img/packing-list.png` — used on the `components` page
- [x] **Shared content is wired in.** `install_os` uses the `sf-shared` page, and
      `appendix` uses the shared VNC and Windows SSH pages. The submodule is at
      `docs/source/_shared`, RTD declares `submodules: include: all`, and CI checks out
      with `submodules: recursive`. `exclude_patterns` in `conf.py` skips the shared
      pages this kit does not use (Fusion HAT, Robot HAT power, I²C/SPI, Blynk,
      FileZilla) and the shared `set_up_pi.rst`, which we replace with our own.
- [x] **`set_up_pi` is a local page.** Taken from `sf-shared` and adapted to this board:
      Mini HDMI adapter instead of micro-HDMI, one USB data port, 2.4 GHz-only Wi-Fi, no
      Ethernet, and the robot-specific note removed.
- [x] **The screen-setup photo is in place.** `img/connect_pc.jpg` shows the Zero 2 W in
      its case wired to a monitor through the Mini HDMI adapter, with the USB data and
      PWR IN cables attached. It replaces the shared Pi 5 picture, which showed ports this
      board does not have.
- [ ] **One more image would be nice.** The retail card covers the cover and the packing
      list, and the kit photos cover ports, case fitting and the screen connection. What is
      left is a flat-lay of the whole kit as unpacked, for `components`. Source photos are
      in the repository's parent directory, in `新建文件夹(12)`.
- [x] **Deleted pages.** Five pages were removed deliberately, so do not re-add them:
  - `assembly` — the case is two plates and four screws, and `img/zero2w_case_install.jpg`
    now shows the whole procedure in `components.rst`.
  - `remote_access` — duplicated. Remote desktop is the shared Appendix page, and
    Raspberry Pi Connect is documented by Raspberry Pi itself.
  - `video` — no video tutorials are planned for this kit.
  - `get_start/quick_start` — every page it linked to is already in the sidebar, so it
    only put a click between the reader and the setup pages.
  - `get_start/connectors` — the shared `set_up_pi` page already says which port takes
    what, and `img/zero2w_port.jpg` in the FAQ labels them all.
- [ ] Reconcile the BOM with the retail card. The card lists **2 large + 2 small
      heatsinks** while the production BOM (A0001440) describes 4 thermal pads; the docs
      currently follow the card, which is what the customer sees. Confirm the distinction
      so the two documents do not drift.
- [ ] Verify the exact screw count in `components.rst` against the current production
      batch. The card says **4 pcs M2×6**, which the docs now follow; recent photos show
      only two in one shot.
- [ ] Confirm which components the two **small** heatsinks cover. `components.rst` says
      "the smaller components next to them" — verify against the case's own instructions.
- [ ] Confirm whether the white foam bag in the photos is extra packaging, and describe it
      if it is not.

## License

Documentation text and images © SunFounder. See the copyright notice on the `index`
page of the published manual.

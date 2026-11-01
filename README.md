# The Other Side of the Fourier Transform

Study notes, series outline, and animation code for a project on **generalized Fourier
transforms**: why a constant has spectrum `2πδ`, why polynomials produce derivatives of `δ`,
why the step function produces a Cauchy principal value, and how tempered distributions make
all of it rigorous.

**Main document:** [`docs/The_Other_Side_of_the_Fourier_Transform.pdf`](docs/The_Other_Side_of_the_Fourier_Transform.pdf) — 54 pages, English.

> **中文简介**
> 这套材料围绕一个朴素的矛盾展开：常数信号显然"只含零频率"，可它的傅里叶积分却发散。
> 六章依次处理常数、多项式、阶跃三个具体对象，再补上收敛性分析、分布的定义，最后在
> 缓增分布上重新定义傅里叶变换，把前面的结果全部证明出来。
> `notes/` 是可编译的 LaTeX 源文件，`outline/` 是系列构思稿，`docs/` 是成品 PDF。

## Contents

| Path | What it is |
|---|---|
| `docs/The_Other_Side_of_the_Fourier_Transform.pdf` | The study notes: definitions, theorems with complete proofs, worked computations, tables, 16 solved exercises |
| `docs/background_knowledge.pdf` | Earlier, shorter background handout (Chinese) that seeded the project |
| `notes/` | LaTeX source of the study notes — buildable, one chapter per file |
| `outline/` | Series outline and per-episode notes (Chinese) |
| `Animations/` | Manim scene source for the video series |
| `archive/` | Superseded Chinese draft (kept for history, not maintained) |

## The mathematics

All of this is proved in the notes, not assumed:

```
F[1]      = 2π δ(ω)
F[t^n]    = 2π i^n δ^(n)(ω)
F[H]      = π δ(ω) + PV(1/(iω))
```

with the convention

```
F[f](ω) = ∫ f(t) e^{-iωt} dt ,     f(t) = (1/2π) ∫ F[f](ω) e^{iωt} dω
```

and pairings that carry no complex conjugation. Chapter 6 derives the transform on the dual of
the Schwartz space; the first three chapters get there by explicit computation with regularizing
families, and the gap between the two is flagged throughout (see Appendix A.6, "where each
statement is proved").

## Building the notes

Requires a TeX distribution with the standard `amsmath`/`amsthm`/`tikz`/`pgfplots` set
(TeX Live 2024+, MacTeX, or MiKTeX). No system fonts, no XeLaTeX — plain `pdflatex` is enough.

```bash
cd notes
make            # or: latexmk -pdf main.tex   /   pdflatex main.tex && pdflatex main.tex
```

The PDF is written to `notes/main.pdf`.

## Repository layout

```
.
├── docs/                  built PDFs
├── notes/                 LaTeX source (main.tex + ch1..ch6 + appA, appB)
├── outline/               series planning documents
├── Animations/delta.py    Manim scene; rendered output is git-ignored
├── archive/               superseded draft
└── .github/workflows/     CI: builds notes/main.pdf on every push
```

## Continuous integration

`.github/workflows/build-notes.yml` builds the PDF on Ubuntu with a TeX Live container and
uploads it as a build artifact, so every push that touches `notes/` is checked for compilation
errors. No secrets or setup are required.

## License

- Prose, figures, and PDFs: **CC BY 4.0** — reuse with attribution.
- Code (`Animations/`, build scripts): **MIT**, see [`LICENSE`](LICENSE).

If you would rather license everything under MIT, replace `LICENSE` and drop the first line above.

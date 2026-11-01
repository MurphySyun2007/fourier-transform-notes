# Build instructions

## Requirements
- XeLaTeX or pdfLaTeX (TeX Live 2024+). The document uses only standard packages:
  amsmath, amssymb, amsthm, mathtools, mathrsfs, geometry, booktabs, tabularx,
  enumitem, tikz, pgfplots, microtype, xcolor, fancyhdr, hyperref, lmodern.
- No system fonts required; the document compiles with pdflatex as well.

## Build
    pdflatex main.tex
    pdflatex main.tex      # second pass for cross-references and the table of contents

(or `latexmk -pdf main.tex`)

Output: main.pdf, 54 pages.

## Files
    main.tex   preamble, title page, preface, chapter inclusion
    ch1.tex    Ch. 1  The Fourier Transform of a Constant
    ch2.tex    Ch. 2  Polynomials and the Derivatives of delta
    ch3.tex    Ch. 3  The Step Function, the Principal Value, and the Missing delta
    ch4.tex    Ch. 4  Limits, Integrals, and Approximate Identities
    ch5.tex    Ch. 5  Distributions
    ch6.tex    Ch. 6  Tempered Distributions and the Generalized Transform
    appA.tex   Appendix A  Tables
    appB.tex   Appendix B  Exercises with Solutions

## Editing notes
- Statement environments: theorem, proposition, lemma, corollary, definition,
  example, exercise, remark. All share one counter, numbered by chapter.
- Every head-line formula is cross-referenced by \label; renaming a result only
  requires changing its label.
- Convention (fixed throughout): F[f](w) = int f(t) e^{-iwt} dt, 2*pi on the
  inverse transform, pairings without complex conjugation.

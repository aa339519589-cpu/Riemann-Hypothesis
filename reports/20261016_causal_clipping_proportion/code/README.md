# Reproducing the explicit causal-clipping scalar certificate

Requirements: Python 3 and official `python-flint` 0.9.0 (FLINT 3.6.0).
No binary, vendored dependency, or author-hosted executable is included.
Run Python without `-O` or `PYTHONOPTIMIZE`.

From this directory run:

```sh
bash reproduce.sh
```

The wrapper verifies the manifest and reruns the finite trigonometric Arb
calculation at 256 and 384 bits. The source recognizes zero frequencies
symbolically and otherwise integrates finite cosine products by closed
formulas. It uses no numerical quadrature. Acceptance requires the final
strict interval comparison `increment_arithmetic_pass: true`; the script
raises an exception otherwise. Output files are local regeneration products.

The exact scientific input is unchanged from the previous certificate:
`certified_window_data.json`, SHA-256
`3aec299878696245945760411329dbcdfd3e49e78c01fbf6bd8b1430f01c78e9`.
It includes all cosine coefficients, pressure and pair-weight integers,
normalizations and the exact accepted reward. No search proposal is a proof
input. The scalar builder is SHA-256
`9e56ad8d5fda0936883cdd59970f879da83182842a66b48cefded0b1ead7629d`.

This small package does not duplicate the earlier exhaustive geometry and
kernel-table certificate. For its complete independent replay use
[the previous package's reproduction command](../../20261016_nine_point_proportion_certificate/code/README.md).
The present inward taper transfers that all-gap inequality by a proved
uniform Fourier error, not by sampling new gaps or importing a search pass.
The copied side-condition JSON pins the old positive margins; its complete
builder/table replay remains in the previous package.

The mathematical report proves the sharp-operator, finite clipping,
explicit causal constant and taper premises separately. The scalar script's
scope label deliberately describes only what that script checks. A scalar
PASS alone is not a zeta proportion theorem, nor a Lean-kernel certificate.

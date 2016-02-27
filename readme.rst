=====================================================
Equajson: equations and metadata stored in JSON files
=====================================================

--------------------------------
Examples of searching equations.
--------------------------------


The normal distribution::

    $ python equajson.py normal
    Normal distribution
              1      ⎛  (x−μ)²⎞
    P(x) = ―――――― exp⎜− ――――――⎟
           σ√(2π)    ⎝    2σ² ⎠
    where:
    P = probability
    x = independent variable
    μ = mean
    σ = standard deviation
    exp = exponential function
    π = 3.14159…
    --------------------------------------------------------------------------------

Schödinger equation::

    $ equajson.py schro
    Schrödinger equation
             ⎛   ℏ²          ⎞     
    E Ψ(r) = ⎜‒ ‒‒‒ ∇² + V(r)⎟ Ψ(r)
             ⎝  2μ           ⎠     
    where:
    E = energy
    Ψ = wave function
    r = radius
    ℏ = reduced Planck constant
    μ = reduced mass
    ∇² = Laplacian
    V = potential energy function
    --------------------------------------------------------------------------------

Laplacian::

    $ python equajson.py lapla
    Laplacian in spherical coordinates
          1 ∂  ⎛  ∂ƒ⎞      1   ∂  ⎛     ∂ƒ⎞      1    ∂²ƒ
    ∇²ƒ = ― ―― ⎜r ――⎟ + ―――――― ―― ⎜sinθ ――⎟ + ――――――― ―――
          r ∂r ⎝  ∂r⎠   r²sinθ ∂θ ⎝     ∂θ⎠   r²sin²θ ∂φ²
    where:
    ∇² = Laplacian
    ƒ = function in spherical coordinates
    r = radius
    ∂ = partial derivative
    θ = zenith angle, spans π radian
    φ = azimuthal angle, spans 2π radian
    --------------------------------------------------------------------------------

Some approximations::

    $ equajson.py approximation
    Stirling's approximation
    n! ≈ nⁿ e⁻ⁿ √(2πn)
    where:
    n = integer of interest
    e = 2.71828…
    π = 3.14159…
    --------------------------------------------------------------------------------
    Linear approximation
    f(x) ≈ f(a) + f'(a)(x-a)
    where:
    x = independent variable
    a = point of tangency
    --------------------------------------------------------------------------------
    Small angle approximation
                  x²
    cos(x) ≈ 1 − ‒‒‒
                  2 
    where:
    cos = cosine function
    x = angle
    --------------------------------------------------------------------------------
    Binomial approximation
    (1+x)ⁿ ≈ 1 + nx
    where:
    x = small real number (|x| ≪ 1)
    n = exponent
    --------------------------------------------------------------------------------

------------
Dependencies
------------

- Searching only:

  - python

- Documentation:

  - docutils
  - markdown

- JSON validation

  - python-jsonschema

----------------
Related projects
----------------

- `PhysIndex <http://www.physindex.com/>`_
- `LaTeXSearch <http://latexsearch.com/>`_
- `The Physics Hypertextbook: Frequently Used Equations <http://physics.info/equations/>`_
- `Search On Math <http://searchonmath.com/>`_
- `EquationSheet.com <http://www.equationsheet.com/>`_
- `Symbolab <https://www.symbolab.com/>`_

.. Advantages over wikipedia: control over parametrization, offline availability, variety of markup languages

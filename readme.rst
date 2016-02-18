======================
Quickly find equations 
======================


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

    $ equajson.py lapla
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

    $ python equajson.py approximation
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
    x = small number (close to 0)
    n = exponent
    --------------------------------------------------------------------------------


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


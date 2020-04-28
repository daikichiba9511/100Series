using PyPlot
using LinearAlgebra
using Statistics
using Random
using Distributions
using PyCall


function min_sq(x::T, y::T) where {T<:AbstractArray} 
    x_bar, y_bar = mean(x), mean(y)
    beta1 = (x .- x_bar) ⋅ (y .- y_bar) / norm(x .- x_bar)^2 #(1.4)
    beta0 = y_bar - beta1 * x_bar
    return beta1, beta0
end


function run()
    N = 100
    d = Normal(2, 1)
    a = rand(d, N)
    b = randn(1)
    x = randn(N)
    y = a .* x .+ b + randn(N)

    a1, b1 = min_sq(x, y)
    xx = x .- mean(x)
    yy = y .- mean(y)
    a2, b2 = min_sq(xx, yy)

    x_seq = -5:0.01:5
    y_pre = x_seq * a1 .+ b1
    yy_pre = x_seq * a2 .+ b2

    # plot 
    fig = figure(figsize=(10,10))
    scatter(x, y, alpha=0.6)
    axhline(0, c="black", linewidth=0.5)
    axvline(0, c="black", linewidth=0.5)
    plot(x_seq, y_pre, label="before Centering")
    plot(x_seq, yy_pre, label="after Centering")
    xlabel("X")
    ylabel("Y")
    grid()
    display(fig)
    savefig("./stats_ml_mathmatical_py/fig/fig1-2_jl.png")
    close(fig)
end


run()
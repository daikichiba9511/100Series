using PyPlot
using Random
using Distributions

# fig1_2にあるmin_sqを使いたい
include("fig1_2.jl")

function main()
    N = 100
    iter_num = 100
    fig = figure(figsize=(10, 10))

    for _ in 1:iter_num
        x = randn(N) .+ 2
        e = randn(N)
        y = x .+ 1 + e
        b_1, b_0 = min_sq(x, y)
        scatter(b_0, b_1)
    end
    
    axhline(1.0, c="black", linewidth=0.5)
    axvline(1.0, c="black", linewidth=0.5)
    xlabel("beta_0")
    ylabel("beta_1")
    grid()
    display(fig)
    savefig("./stats_ml_mathmatical_py/fig/fig1_4_jl.png")
    close(fig)
end

# main
main()
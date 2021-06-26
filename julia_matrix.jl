## Modules Imported
using DelimitedFiles
## Creating the Matrix Function
function matrix_create(n, m)
    """This function takes in the desired dimensions for the matrices and creates
    two random matrices full of integers from 0 to 10. 
    The matrices created are always able to be multiplied together.
    n = size of first dimension
    m = size of second dimension
    returns: two random matrices
    """
    a = rand(0:10, n, m)
    b = rand(0:10, m, n)
    return a, b
end
## Running a for loop that iterates through different sized matrices
julia_times = []
for i in (100:100:3000)
    a, b = matrix_create(i, i)
    c = @elapsed a * b
    append!(julia_times, c)
    print("Time for calculation of $i x $i matrix:")
    @time a * b 
end
##
writedlm( "JuliaTimes.csv",  julia_times, ',')
##

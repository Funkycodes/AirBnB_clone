function Recursive_exponent(base, power)
    if power == 0 then
        return 1
    else
        return base * Recursive_exponent(base, power - 1)
    end
end

local expo = Recursive_exponent(2, 8)
print(expo)



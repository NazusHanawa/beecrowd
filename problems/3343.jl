
function get_inputs()
    total_titans, max_wall_size = parse.(Int, split(readline()))
    titan_str = readline()
    small_size, medium_size, large_size = parse.(Int, split(readline()))

    return total_titans, max_wall_size, titan_str, small_size, medium_size, large_size
end

function get_minimum_amount_of_walls(total_titans, titan_str, max_wall_size, small, medium, large)
    max_walls = 1 + total_titans ÷ (max_wall_size ÷ large)
    walls_size = fill(max_wall_size, max_walls)

    titan_pos_small = 1
    titan_pos_medium = 1
    titan_pos_large = 1

    for titan in titan_str
        if titan == 'P'
            titan_size = small
            current_pos = titan_pos_small
        elseif titan == 'M'
            titan_size = medium
            current_pos = titan_pos_medium
        else
            titan_size = large
            current_pos = titan_pos_large
        end

        while true
            if titan_size <= walls_size[current_pos]
                walls_size[current_pos] -= titan_size
                break
            else
                current_pos += 1
            end
        end

        if titan == 'P'
            titan_pos_small = current_pos
        elseif titan == 'M'
            titan_pos_medium = current_pos
        else
            titan_pos_large = current_pos
        end
    end
    
    return max(titan_pos_small, titan_pos_medium, titan_pos_large)
end

function main()
    total_titans, max_wall_size, titan_str, small, medium, large = get_inputs()

    minimum_walls = get_minimum_amount_of_walls(
        total_titans,
        titan_str,
        max_wall_size,
        small,
        medium,
        large
    )

    println(minimum_walls)
end

main()
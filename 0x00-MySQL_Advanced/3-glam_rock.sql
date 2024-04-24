-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, COALESCE(`split`, 2022) - formed as lifespan FROM metal_bands WHERE FIND_IN_SET("Glam rock", style) > 0;	

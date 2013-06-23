from cargo import Cargo

cargo = Cargo(id = 'coffee',
              number = '15',
              type_name = 'string(STR_CARGO_NAME_COFFEE)',
              unit_name = 'string(STR_CARGO_NAME_COFFEE)',
              type_abbreviation = '156',
              sprite = 'NEW_CARGO_SPRITE',
              weight = '1.0',
              station_list_colour = '82',
              cargo_payment_list_colour = '82',
              is_freight = '1',
              cargo_classes = 'bitmask(CC_EXPRESS, CC_PIECE_GOODS, CC_REFRIGERATED)',
              cargo_label = '"FRVG"',
              town_growth_effect = 'TOWNGROWTH_NONE',
              town_growth_multiplier = '1.0',
              units_of_cargo = '80',
              items_of_cargo = 'string(STR_CARGO_UNIT_COFFEE)',
              penalty_lowerbound = '0',
              single_penalty_length = '26',
              price_factor = '119.696617126',
              capacity_multiplier = '1',
              icon_indices = (14, 0))

cargo.economy_variations['FIRS']['disabled'] = True
cargo.economy_variations['BASIC_ARCTIC']['disabled'] = True
cargo.economy_variations['BASIC_TROPIC']['disabled'] = True
cargo.economy_variations['BASIC_TEMPERATE']['disabled'] = True

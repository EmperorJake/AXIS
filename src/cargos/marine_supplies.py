from cargo import Cargo

cargo = Cargo(id = 'marine_supplies',
              type_name = 'string(STR_CARGO_NAME_MARINE_SUPPLIES)',
              unit_name = 'string(STR_CARGO_NAME_MARINE_SUPPLIES)',
              type_abbreviation = 'string(STR_CID_MARINE_SUPPLIES)',
              sprite = 'NEW_CARGO_SPRITE',
              weight = '0.625',
              station_list_colour = '79',
              cargo_payment_list_colour = '79',
              is_freight = '1',
              cargo_classes = 'bitmask(CC_EXPRESS, CC_PIECE_GOODS)',
              cargo_label = 'SESP',
              town_growth_effect = 'TOWNGROWTH_NONE',
              town_growth_multiplier = '1.0',
              units_of_cargo = '84',
              items_of_cargo = 'string(STR_CARGO_UNIT_MARINE_SUPPLIES)',
              penalty_lowerbound = '6',
              single_penalty_length = '36',
              price_factor = '140.58637619',
              capacity_multiplier = '1',
              icon_indices = (11, 1))

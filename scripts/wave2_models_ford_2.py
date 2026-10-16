"""
Wave 2 Deep-Dive Model Data: Ford Performance, Icons, and Trucks (Part 2)
Models:
17. Focus
18. Mustang
19. Everest
20. F-Series
"""
from typing import Any, Dict

MODEL_FOCUS: Dict[str, Any] = {
    "make_slug": "ford",
    "model_slug": "focus",
    "name": "Ford Focus",
    "vehicle_type": "Hatchback / Sedan / Wagon",
    "segment": "Small",
    "years_sold_au": {"start": 2002, "end": 2022},
    "locally_built": False,
    "assembly_plants_au": [
        "Imported (Saarlouis, Germany)",
        "Imported (Valencia, Spain)",
        "Imported (Rayong, Thailand, LW 2012-2015)"
    ],
    "overview": "The Ford Focus replaced the Laser in 2002 and immediately established itself as Australia's benchmark dynamic driver's car in the compact segment thanks to its revolutionary 'Control Blade' multi-link rear suspension. Across four generations (LR, LT/LV, LW/LZ, and SA), the Focus earned critical acclaim. For Australian car enthusiasts, the Focus name was cemented by legendary performance flagships: the 2.0L high-revving LR ST170 (127 kW), the five-cylinder turbo LT/LV XR5 Turbo (166 kW 2.5L Volvo turbo) and limited-edition 224 kW Focus RS, the sensational 257 kW drift-mode AWD LZ Focus RS, and the nimble SA Focus ST.",
    "australian_market_notes": "The LT/LV Focus XR5 Turbo achieved massive cult status in Australia, embraced for the thunderous 5-cylinder warble of its turbocharged engine and exceptional chassis composure. In 2016, the LZ Focus RS created a national sensation when all 500 Australian allocation units sold out in days, driven by its 257 kW twin-scroll turbo engine and headline-grabbing 'Drift Mode' all-wheel drive.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "LR",
            "generation_name": "LR Focus & ST170",
            "years": {"start": 2002, "end": 2005},
            "body_styles": ["3-door hatchback", "5-door hatchback", "4-door sedan"],
            "platform": "Ford C170 platform",
            "ancap_rating": 4,
            "summary": "First Australian Focus. Groundbreaking Control Blade independent rear suspension, sharp New Edge styling, and the acclaimed 127 kW ST170 hot hatch.",
            "engines": [
                {
                    "engine_code": "Duratec-ST-2.0L",
                    "name": "Ford Duratec ST 2.0L DOHC 16V Inline-4",
                    "displacement_cc": 1988,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 127.0,
                    "power_rpm": "7000",
                    "torque_nm": 196.0,
                    "torque_rpm": "5500",
                    "compression_ratio": "10.2:1",
                    "valvetrain": "DOHC 16V VVT",
                    "notes": "Cosworth-developed cylinder head, dual-stage intake manifold; paired with 6-speed Getrag manual."
                }
            ],
            "badges": [
                {
                    "badge_name": "ST170",
                    "years": {"start": 2003, "end": 2005},
                    "body_styles": ["3-door hatchback"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed manual Getrag MT285"],
                    "msrp_aud_min": 37000,
                    "msrp_aud_max": 38990,
                    "fuel_consumption_l_100km": 9.1,
                    "kerb_weight_kg": 1280,
                    "standard_features": [
                        "127 kW 2.0L Duratec ST engine (7200 rpm redline)",
                        "17-inch multi-spoke alloy wheels",
                        "300mm front disc brakes",
                        "Half-leather sports bucket seats",
                        "Oil temperature and oil pressure auxiliary gauges"
                    ],
                    "notes": "Cosworth-engineered hot hatch benchmark."
                }
            ],
            "configurations": [
                {
                    "badge_name": "ST170",
                    "body_style": "3-door hatchback",
                    "engine_code": "Duratec-ST-2.0L",
                    "transmission": "6-speed manual Getrag MT285",
                    "drivetrain": "FWD",
                    "msrp_aud": 37000,
                    "power_kw": 127.0,
                    "torque_nm": 196.0,
                    "fuel_l_100km": 9.1,
                    "towing_braked_kg": 1200,
                    "notes": "127 kW 6-speed manual driver's car."
                }
            ]
        },
        {
            "series_code": "LT-LV",
            "generation_name": "LT / LV Focus & XR5 Turbo / RS",
            "years": {"start": 2005, "end": 2011},
            "body_styles": ["3-door hatchback", "5-door hatchback", "4-door sedan"],
            "platform": "Ford C1 platform",
            "ancap_rating": 5,
            "summary": "Second-generation Focus. Massive Australian success with the 166 kW 2.5L 5-cylinder turbo Focus XR5 Turbo and the 224 kW RevoKnuckle Focus RS.",
            "engines": [
                {
                    "engine_code": "Duratec-2.5T-Volvo",
                    "name": "Ford / Volvo 2.5L 20V DOHC Turbo Inline-5",
                    "displacement_cc": 2522,
                    "displacement_litres": 2.5,
                    "cylinders": 5,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Petrol",
                    "power_kw": 166.0,
                    "power_rpm": "6000",
                    "torque_nm": 320.0,
                    "torque_rpm": "1600",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "DOHC 20V VVT",
                    "notes": "BorgWarner K04 turbocharger; distinctive 5-cylinder warble; powers XR5 Turbo."
                },
                {
                    "engine_code": "Duratec-RS-2.5T",
                    "name": "Ford RS 2.5L 20V DOHC High-Output Turbo Inline-5",
                    "displacement_cc": 2522,
                    "displacement_litres": 2.5,
                    "cylinders": 5,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Petrol",
                    "power_kw": 224.0,
                    "power_rpm": "6500",
                    "torque_nm": 440.0,
                    "torque_rpm": "2300",
                    "compression_ratio": "8.5:1",
                    "valvetrain": "DOHC 20V",
                    "notes": "BorgWarner K16 turbocharger, 1.4 bar boost, Quaife automatic torque-biasing helical LSD; 224 kW (305 PS)."
                }
            ],
            "badges": [
                {
                    "badge_name": "XR5 Turbo",
                    "years": {"start": 2006, "end": 2011},
                    "body_styles": ["5-door hatchback"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed manual M66"],
                    "msrp_aud_min": 35990,
                    "msrp_aud_max": 39990,
                    "fuel_consumption_l_100km": 9.3,
                    "kerb_weight_kg": 1442,
                    "standard_features": [
                        "166 kW 2.5L 5-cylinder turbo engine",
                        "Recaro two-tone sports bucket seats",
                        "Triple dash gauge pod (turbo boost, oil pressure, oil temperature)",
                        "18-inch 5-spoke alloy wheels and dual sports exhausts",
                        "Lowered sports chassis with ESP"
                    ],
                    "notes": "Legendary Australian hot hatch favorite."
                },
                {
                    "badge_name": "Focus RS",
                    "years": {"start": 2010, "end": 2010},
                    "body_styles": ["3-door hatchback"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed manual M66 with Quaife LSD"],
                    "msrp_aud_min": 59990,
                    "msrp_aud_max": 59990,
                    "fuel_consumption_l_100km": 10.4,
                    "kerb_weight_kg": 1467,
                    "standard_features": [
                        "224 kW (305 hp) high-boost 2.5L 5-cylinder turbo",
                        "RevoKnuckle front suspension eliminating torque steer",
                        "Quaife automatic torque-biasing limited-slip differential",
                        "19-inch 15-spoke RS alloy wheels and massive 336mm ventilated discs",
                        "Recaro motorsport shell bucket seats and twin-blade rear wing"
                    ],
                    "notes": "Extremely rare collector model; strictly 315 imported to Australia."
                }
            ],
            "configurations": [
                {
                    "badge_name": "XR5 Turbo",
                    "body_style": "5-door hatchback",
                    "engine_code": "Duratec-2.5T-Volvo",
                    "transmission": "6-speed manual M66",
                    "drivetrain": "FWD",
                    "msrp_aud": 35990,
                    "power_kw": 166.0,
                    "torque_nm": 320.0,
                    "fuel_l_100km": 9.3,
                    "towing_braked_kg": 1300,
                    "notes": "Iconic 5-cylinder 6-speed manual hot hatch."
                },
                {
                    "badge_name": "Focus RS",
                    "body_style": "3-door hatchback",
                    "engine_code": "Duratec-RS-2.5T",
                    "transmission": "6-speed manual M66 with Quaife LSD",
                    "drivetrain": "FWD",
                    "msrp_aud": 59990,
                    "power_kw": 224.0,
                    "torque_nm": 440.0,
                    "fuel_l_100km": 10.4,
                    "towing_braked_kg": 1000,
                    "notes": "224 kW RevoKnuckle hyper-hatch."
                }
            ]
        },
        {
            "series_code": "LW-LZ",
            "generation_name": "LW / LZ Focus & ST / RS AWD",
            "years": {"start": 2011, "end": 2018},
            "body_styles": ["5-door hatchback"],
            "platform": "Ford Global C-car platform",
            "ancap_rating": 5,
            "summary": "Third-generation Focus. High-technology EcoBoost turbo engines, 184 kW Focus ST, and the earth-shattering 257 kW Focus RS AWD with Drift Mode.",
            "engines": [
                {
                    "engine_code": "EcoBoost-2.0T-ST",
                    "name": "Ford EcoBoost 2.0L Direct-Injection Turbo Inline-4",
                    "displacement_cc": 1999,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Petrol",
                    "power_kw": 184.0,
                    "power_rpm": "5500",
                    "torque_nm": 360.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "9.3:1",
                    "valvetrain": "DOHC 16V Ti-VCT",
                    "notes": "Direct injection turbo with overboost function to 360 Nm; powers Focus ST."
                },
                {
                    "engine_code": "EcoBoost-2.3T-RS",
                    "name": "Ford EcoBoost 2.3L Twin-Scroll Turbo Inline-4",
                    "displacement_cc": 2261,
                    "displacement_litres": 2.3,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Petrol",
                    "power_kw": 257.0,
                    "power_rpm": "6000",
                    "torque_nm": 440.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "9.4:1",
                    "valvetrain": "DOHC 16V Ti-VCT",
                    "notes": "High-tensile cast alloy head, twin-scroll turbo with 470 Nm overboost; powers Focus RS AWD."
                }
            ],
            "badges": [
                {
                    "badge_name": "Focus ST",
                    "years": {"start": 2012, "end": 2018},
                    "body_styles": ["Hatchback"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed manual"],
                    "msrp_aud_min": 38290,
                    "msrp_aud_max": 38990,
                    "fuel_consumption_l_100km": 7.3,
                    "kerb_weight_kg": 1425,
                    "standard_features": [
                        "184 kW 2.0L EcoBoost turbo engine",
                        "Recaro leather-accented sports seats",
                        "Enhanced Torque Vectoring Control and variable-ratio sports steering",
                        "Center-exit dual hexagonal exhaust",
                        "SYNC connectivity with satellite navigation"
                    ],
                    "notes": "High-performance hot hatch."
                },
                {
                    "badge_name": "Focus RS (AWD)",
                    "years": {"start": 2016, "end": 2018},
                    "body_styles": ["Hatchback"],
                    "drivetrain": "AWD",
                    "transmissions": ["6-speed manual"],
                    "msrp_aud_min": 50990,
                    "msrp_aud_max": 56990,
                    "fuel_consumption_l_100km": 8.1,
                    "kerb_weight_kg": 1575,
                    "standard_features": [
                        "257 kW 2.3L EcoBoost Twin-Scroll Turbo (0-100 km/h in 4.7s)",
                        "Ford Performance All-Wheel Drive with Dynamic Torque Vectoring",
                        "Selectable Drive Modes including industry-first 'Drift Mode' and 'Launch Control'",
                        "Brembo 4-piston front brake calipers and Ohlins two-stage adjustable dampers",
                        "Recaro shell seats and 19-inch forged alloy wheels"
                    ],
                    "notes": "All-wheel-drive hyper-hatch sensation."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Focus RS (AWD)",
                    "body_style": "Hatchback",
                    "engine_code": "EcoBoost-2.3T-RS",
                    "transmission": "6-speed manual",
                    "drivetrain": "AWD",
                    "msrp_aud": 50990,
                    "power_kw": 257.0,
                    "torque_nm": 440.0,
                    "fuel_l_100km": 8.1,
                    "towing_braked_kg": 1000,
                    "notes": "257 kW Drift Mode AWD hyper-hatch."
                }
            ]
        }
    ]
}

MODEL_MUSTANG: Dict[str, Any] = {
    "make_slug": "ford",
    "model_slug": "mustang",
    "name": "Ford Mustang",
    "vehicle_type": "Fastback Coupe / Convertible",
    "segment": "Sports / Muscle Car",
    "years_sold_au": {"start": 1965, "end": 2026},
    "locally_built": True,
    "assembly_plants_au": [
        "Homebush, New South Wales (1965-1966 RHD factory conversions)",
        "Campbellfield, Victoria (Tickford TVE SVT Cobra conversions, 2001-2002)",
        "Flat Rock, Michigan, USA (Factory RHD export to Australia, 2015-present)"
    ],
    "overview": "The Ford Mustang has a storied heritage in Australia stretching back six decades. In 1965, Ford Australia officially imported and converted 400 iconic 1965-1966 notchback Mustangs to right-hand drive at Homebush, NSW, while touring car legend Norm Beechey campaigned a 1965 Mustang to Australia's first Australian Touring Car Championship win for an American V8. In 2001, Ford Tickford Experience (FTE) in Campbellfield, Victoria undertook a heroic $4 million engineering program to convert 250 SVT Mustang Cobras featuring independent rear suspension and 240 kW 4.6L DOHC 32V modular V8s. In late 2015, Ford delivered the first global factory right-hand drive FM Mustang to Australia, creating unprecedented multi-year customer waiting lists. The FM/FN generations and all-new 2024+ S650 generation (featuring the 362 kW 5.0L Gen-4 Coyote V8 and 373 kW Dark Horse) made Mustang Australia's best-selling sports car for seven consecutive years.",
    "australian_market_notes": "The 2001 Tickford Cobra conversion was a monumental engineering triumph: TVE completely re-engineered the front floor pan, steering rack, wiring harness, and air conditioning to OEM right-hand drive standards, winning full compliance approval under Australian Design Rules. In modern times, the Mustang represents Ford Australia's primary weapon in Supercars Championship touring car racing, carrying the blue oval flag across Mount Panorama.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "First-Gen-AU",
            "generation_name": "First Generation Mustang (Australian Delivery)",
            "years": {"start": 1965, "end": 1973},
            "body_styles": ["2-door hardtop coupe", "2-door fastback"],
            "platform": "Ford Falcon unibody architecture",
            "ancap_rating": None,
            "summary": "Official 1965-66 Ford Australia Homebush RHD conversions and private imports. Won the 1965 Australian Touring Car Championship with Norm Beechey.",
            "engines": [
                {
                    "engine_code": "Windsor-289-V8",
                    "name": "Ford 289ci (4.7L) Challenger V8",
                    "displacement_cc": 4727,
                    "displacement_litres": 4.7,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 149.0,
                    "power_rpm": "4400",
                    "torque_nm": 382.0,
                    "torque_rpm": "2400",
                    "compression_ratio": "9.3:1",
                    "valvetrain": "OHV 16V",
                    "notes": "2-barrel carburettor; 200 bhp rating in 1965-66 Australian deliveries."
                }
            ],
            "badges": [
                {
                    "badge_name": "Mustang Hardtop (AU)",
                    "years": {"start": 1965, "end": 1966},
                    "body_styles": ["Coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed Cruise-O-Matic automatic", "4-speed manual floor"],
                    "msrp_aud_min": 3990,
                    "msrp_aud_max": 4450,
                    "fuel_consumption_l_100km": 14.5,
                    "kerb_weight_kg": 1270,
                    "standard_features": [
                        "289ci Challenger V8 engine",
                        "Right-hand drive Homebush factory conversion",
                        "Front bucket seats and center console",
                        "Power-assisted steering and front disc brakes"
                    ],
                    "notes": "Historical factory-backed Australian delivery; 400 imported."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Mustang Hardtop (AU)",
                    "body_style": "Coupe",
                    "engine_code": "Windsor-289-V8",
                    "transmission": "3-speed Cruise-O-Matic automatic",
                    "drivetrain": "RWD",
                    "msrp_aud": 4200,
                    "power_kw": 149.0,
                    "torque_nm": 382.0,
                    "fuel_l_100km": 14.5,
                    "towing_braked_kg": 1000,
                    "notes": "Official 1965 Australian delivery V8."
                }
            ]
        },
        {
            "series_code": "SN-95-Tickford",
            "generation_name": "SN-95 Tickford Mustang SVT Cobra",
            "years": {"start": 2001, "end": 2002},
            "body_styles": ["2-door coupe", "2-door convertible"],
            "platform": "Ford Fox-4 platform with Independent Rear Suspension (IRS)",
            "ancap_rating": None,
            "summary": "Hand-built right-hand drive conversion by Tickford Vehicle Engineering (TVE) in Campbellfield, Victoria. 240 kW 4.6L hand-assembled DOHC 32V modular V8.",
            "engines": [
                {
                    "engine_code": "Modular-4.6-DOHC-32V",
                    "name": "Ford SVT Modular 4.6L DOHC 32V V8",
                    "displacement_cc": 4601,
                    "displacement_litres": 4.6,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 240.0,
                    "power_rpm": "6000",
                    "torque_nm": 430.0,
                    "torque_rpm": "4750",
                    "compression_ratio": "9.85:1",
                    "valvetrain": "DOHC 32V",
                    "notes": "Hand-built at Ford Romeo Engine Plant with signed plaque; aluminum block with 6800 rpm redline."
                }
            ],
            "badges": [
                {
                    "badge_name": "Mustang SVT Cobra Coupe",
                    "years": {"start": 2001, "end": 2002},
                    "body_styles": ["Coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual Tremec T-45 / TR-3650"],
                    "msrp_aud_min": 85000,
                    "msrp_aud_max": 89000,
                    "fuel_consumption_l_100km": 13.5,
                    "kerb_weight_kg": 1555,
                    "standard_features": [
                        "240 kW hand-built DOHC 32V V8",
                        "Multi-link Independent Rear Suspension (IRS)",
                        "17-inch cast alloy wheels with 245/45 tyres",
                        "Brembo 330mm front disc brakes",
                        "Leather sports bucket seats with embossed running Cobra emblem",
                        "Mach 460 premium 8-speaker audio system"
                    ],
                    "notes": "Tickford-converted Campbellfield hero; only 250 built."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Mustang SVT Cobra Coupe",
                    "body_style": "Coupe",
                    "engine_code": "Modular-4.6-DOHC-32V",
                    "transmission": "5-speed manual Tremec T-45 / TR-3650",
                    "drivetrain": "RWD",
                    "msrp_aud": 85000,
                    "power_kw": 240.0,
                    "torque_nm": 430.0,
                    "fuel_l_100km": 13.5,
                    "towing_braked_kg": 1000,
                    "notes": "Tickford Australian factory RHD Cobra."
                }
            ]
        },
        {
            "series_code": "FM-FN",
            "generation_name": "FM / FN Mustang (S550)",
            "years": {"start": 2015, "end": 2023},
            "body_styles": ["2-door fastback coupe", "2-door convertible"],
            "platform": "Ford S550 platform",
            "ancap_rating": 3,
            "summary": "First global factory right-hand drive Mustang. Multi-link IRS, 2.3L EcoBoost turbo, 5.0L Coyote V8 up to 339 kW, and track-focused Bullitt and Mach 1 editions.",
            "engines": [
                {
                    "engine_code": "Coyote-5.0-V8-Gen3",
                    "name": "Ford Coyote 5.0L Dual-Fuel DOHC 32V V8",
                    "displacement_cc": 5038,
                    "displacement_litres": 5.0,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 339.0,
                    "power_rpm": "7000",
                    "torque_nm": 556.0,
                    "torque_rpm": "4600",
                    "compression_ratio": "12.0:1",
                    "valvetrain": "DOHC 32V Ti-VCT",
                    "notes": "Direct and port dual-fuel injection; 7500 rpm redline; active valve performance exhaust."
                }
            ],
            "badges": [
                {
                    "badge_name": "GT Fastback (5.0L V8)",
                    "years": {"start": 2015, "end": 2023},
                    "body_styles": ["Coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed manual Getrag MT-82 with rev matching", "10-speed automatic with paddle shifters"],
                    "msrp_aud_min": 57490,
                    "msrp_aud_max": 66990,
                    "fuel_consumption_l_100km": 12.7,
                    "kerb_weight_kg": 1732,
                    "standard_features": [
                        "339 kW 5.0L Coyote V8",
                        "Brembo 6-piston front brake calipers with 380mm discs",
                        "Active valve dual exhaust with quad tips",
                        "19-inch Ebony Black alloy wheels",
                        "MagneRide magnetorheological adaptive damping option",
                        "12-inch digital customisable instrument cluster"
                    ],
                    "notes": "Australia's top-selling sports car."
                }
            ],
            "configurations": [
                {
                    "badge_name": "GT Fastback (5.0L V8)",
                    "body_style": "Coupe",
                    "engine_code": "Coyote-5.0-V8-Gen3",
                    "transmission": "6-speed manual Getrag MT-82 with rev matching",
                    "drivetrain": "RWD",
                    "msrp_aud": 64190,
                    "power_kw": 339.0,
                    "torque_nm": 556.0,
                    "fuel_l_100km": 13.0,
                    "towing_braked_kg": 1000,
                    "notes": "339 kW 5.0L V8 6-speed manual muscle coupe."
                }
            ]
        },
        {
            "series_code": "S650",
            "generation_name": "S650 Next-Gen Mustang",
            "years": {"start": 2024, "end": 2026},
            "body_styles": ["2-door fastback coupe", "2-door convertible"],
            "platform": "Ford S650 platform",
            "ancap_rating": None,
            "summary": "Next-Gen Mustang featuring fighter-jet inspired cockpit with twin curved displays, 362 kW Gen-4 Coyote V8, Electronic Drift Brake, and the flagship 373 kW Dark Horse.",
            "engines": [
                {
                    "engine_code": "Coyote-5.0-Gen4-DarkHorse",
                    "name": "Ford Coyote 5.0L Gen-4 High-Output DOHC 32V V8",
                    "displacement_cc": 5038,
                    "displacement_litres": 5.0,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 373.0,
                    "power_rpm": "7250",
                    "torque_nm": 567.0,
                    "torque_rpm": "4900",
                    "compression_ratio": "12.0:1",
                    "valvetrain": "DOHC 32V Ti-VCT",
                    "notes": "Dual throttle body induction, forged connecting rods from Shelby GT500; 500 hp output."
                }
            ],
            "badges": [
                {
                    "badge_name": "Dark Horse",
                    "years": {"start": 2024, "end": 2026},
                    "body_styles": ["Coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed manual Tremec TR-3160", "10-speed automatic"],
                    "msrp_aud_min": 99102,
                    "msrp_aud_max": 103002,
                    "fuel_consumption_l_100km": 13.2,
                    "kerb_weight_kg": 1805,
                    "standard_features": [
                        "373 kW (500 hp) Gen-4 Coyote V8 with dual throttle bodies",
                        "Tremec TR-3160 6-speed manual with 3D-printed titanium shift ball",
                        "MagneRide active suspension with heavy-duty front strut tower brace",
                        "Torsen limited-slip differential and auxiliary oil coolers",
                        "Electronic Drift Brake (in partnership with Vaughn Gittin Jr.)",
                        "19-inch staggered alloy wheels and Pirelli P-Zero Trofeo RS tyres"
                    ],
                    "notes": "Track-focused factory flagship."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Dark Horse",
                    "body_style": "Coupe",
                    "engine_code": "Coyote-5.0-Gen4-DarkHorse",
                    "transmission": "6-speed manual Tremec TR-3160",
                    "drivetrain": "RWD",
                    "msrp_aud": 99102,
                    "power_kw": 373.0,
                    "torque_nm": 567.0,
                    "fuel_l_100km": 13.2,
                    "towing_braked_kg": 1000,
                    "notes": "500 hp Tremec manual track monster."
                }
            ]
        }
    ]
}

MODEL_EVEREST: Dict[str, Any] = {
    "make_slug": "ford",
    "model_slug": "everest",
    "name": "Ford Everest",
    "vehicle_type": "Body-on-Frame 7-Seat 4WD SUV",
    "segment": "Large SUV / 4WD",
    "years_sold_au": {"start": 2015, "end": 2026},
    "locally_built": False,
    "assembly_plants_au": [
        "Imported (Rayong, Thailand - Engineered at Campbellfield & You Yangs Proving Ground, Victoria)"
    ],
    "overview": "While built at AutoAlliance Thailand in Rayong, the Ford Everest was conceived, designed, engineered, and durability-tested in Australia by Ford's 2,000-strong global product development hub at Campbellfield and the You Yangs Proving Ground. Developed concurrently with the Ranger ute, the Everest transformed the T6 ladder-frame architecture into a refined 7-seat family wagon featuring coil-sprung Watt's linkage rear suspension, electronic terrain management, and 3.1-tonne towing. The 2015 UA series launched with the rugged 3.2L 5-cylinder Duratorq turbo-diesel and later 2.0L Bi-Turbo with 10-speed auto. The 2022+ UB Next-Gen Everest elevated the platform into an opulent, class-leading 4WD with standard 3.5-tonne towing and a flagship 3.0L V6 Turbo Diesel producing 184 kW and 600 Nm.",
    "australian_market_notes": "The Everest effectively succeeded the Australian-built Ford Territory as Ford's family SUV champion, adding genuine outback off-road capability (800mm water wading) that the car-based Territory could never match. Australian suspension engineers spent thousands of hours tuning the Watt's linkage rear axle on Australian gravel, dirt, and corrugations to achieve an unprecedented blend of highway ride isolation and cornering grip.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "UA",
            "generation_name": "UA Everest",
            "years": {"start": 2015, "end": 2022},
            "body_styles": ["5-door 7-seat SUV"],
            "platform": "Ford T6 platform (Australian developed)",
            "ancap_rating": 5,
            "summary": "First-generation Australian-engineered Everest. Ladder-frame chassis with coil-sprung Watt's linkage rear suspension, 3.2L 5-cyl diesel, and later 2.0L Bi-Turbo 10-speed.",
            "engines": [
                {
                    "engine_code": "Duratorq-3.2-TDCi",
                    "name": "Ford Duratorq 3.2L 5-Cylinder Turbo Diesel",
                    "displacement_cc": 3198,
                    "displacement_litres": 3.2,
                    "cylinders": 5,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Diesel",
                    "power_kw": 143.0,
                    "power_rpm": "3000",
                    "torque_nm": 470.0,
                    "torque_rpm": "1750",
                    "compression_ratio": "15.7:1",
                    "valvetrain": "DOHC 20V",
                    "notes": "Proven inline-five turbo diesel; paired with 6-speed 6R80 automatic."
                },
                {
                    "engine_code": "EcoBlue-2.0-BiTurbo",
                    "name": "Ford EcoBlue 2.0L Bi-Turbo Diesel Inline-4",
                    "displacement_cc": 1996,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Twin-Turbocharged",
                    "fuel_type": "Diesel",
                    "power_kw": 157.0,
                    "power_rpm": "3750",
                    "torque_nm": 500.0,
                    "torque_rpm": "1750",
                    "compression_ratio": "16.0:1",
                    "valvetrain": "DOHC 16V",
                    "notes": "Sequential twin-turbo with 10-speed 10R80 automatic transmission."
                }
            ],
            "badges": [
                {
                    "badge_name": "Titanium 4WD",
                    "years": {"start": 2015, "end": 2022},
                    "body_styles": ["7-seat SUV"],
                    "drivetrain": "4WD",
                    "transmissions": ["6-speed automatic 6R80", "10-speed automatic 10R80"],
                    "msrp_aud_min": 72990,
                    "msrp_aud_max": 76990,
                    "fuel_consumption_l_100km": 7.1,
                    "kerb_weight_kg": 2477,
                    "standard_features": [
                        "Terrain Management System with electronic locking rear differential",
                        "20-inch alloy wheels and panoramic glass roof",
                        "Leather 7-passenger seating with power-folding 3rd row",
                        "Adaptive cruise control, lane keep assist, and autonomous emergency braking",
                        "Semi-autonomous active park assist"
                    ],
                    "notes": "Flagship luxury family off-roader."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Titanium 4WD",
                    "body_style": "7-seat SUV",
                    "engine_code": "EcoBlue-2.0-BiTurbo",
                    "transmission": "10-speed automatic 10R80",
                    "drivetrain": "4WD",
                    "msrp_aud": 73990,
                    "power_kw": 157.0,
                    "torque_nm": 500.0,
                    "fuel_l_100km": 7.1,
                    "towing_braked_kg": 3100,
                    "notes": "500 Nm twin-turbo 10-speed 7-seat wagon."
                }
            ]
        },
        {
            "series_code": "UB-Next-Gen",
            "generation_name": "UB Next-Gen Everest",
            "years": {"start": 2022, "end": 2026},
            "body_styles": ["5-door 7-seat SUV"],
            "platform": "Ford T6.2 platform (Australian engineered)",
            "ancap_rating": 5,
            "summary": "Next-Gen Australian engineering benchmark. 50mm wider track, 3.5-tonne towing, 12-inch portrait touchscreen, and the formidable 3.0L V6 Turbo Diesel.",
            "engines": [
                {
                    "engine_code": "PowerStroke-3.0-V6",
                    "name": "Ford Power Stroke 3.0L V6 Turbo Diesel",
                    "displacement_cc": 2993,
                    "displacement_litres": 3.0,
                    "cylinders": 6,
                    "configuration": "V",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Diesel",
                    "power_kw": 184.0,
                    "power_rpm": "3250",
                    "torque_nm": 600.0,
                    "torque_rpm": "1750",
                    "compression_ratio": "16.0:1",
                    "valvetrain": "DOHC 24V",
                    "notes": "Compacted graphite iron (CGI) block, variable geometry turbo; paired with 10-speed auto and full-time 4WD."
                }
            ],
            "badges": [
                {
                    "badge_name": "Platinum V6 4WD",
                    "years": {"start": 2022, "end": 2026},
                    "body_styles": ["7-seat SUV"],
                    "drivetrain": "4WD",
                    "transmissions": ["10-speed automatic 10R80"],
                    "msrp_aud_min": 77690,
                    "msrp_aud_max": 81140,
                    "fuel_consumption_l_100km": 8.5,
                    "kerb_weight_kg": 2492,
                    "standard_features": [
                        "184 kW / 600 Nm 3.0L V6 Turbo Diesel",
                        "Full-time active all-wheel drive with low range",
                        "21-inch machine-face alloy wheels",
                        "Quilted premium leather seats with heating and ventilation",
                        "12.4-inch digital instrument cluster and 12-inch portrait SYNC 4A screen",
                        "Matrix LED headlights and 360-degree camera with trail view"
                    ],
                    "notes": "Prestige flagship competitor to Toyota LandCruiser Prado."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Platinum V6 4WD",
                    "body_style": "7-seat SUV",
                    "engine_code": "PowerStroke-3.0-V6",
                    "transmission": "10-speed automatic 10R80",
                    "drivetrain": "4WD",
                    "msrp_aud": 79490,
                    "power_kw": 184.0,
                    "torque_nm": 600.0,
                    "fuel_l_100km": 8.5,
                    "towing_braked_kg": 3500,
                    "notes": "184 kW 600 Nm V6 diesel 3.5-tonne tow vehicle."
                }
            ]
        }
    ]
}

MODEL_F_SERIES: Dict[str, Any] = {
    "make_slug": "ford",
    "model_slug": "f-series",
    "name": "Ford F-Series (F-100 / F-250 / F-350 / F-150)",
    "vehicle_type": "Full-size Pickup Truck / Cab Chassis",
    "segment": "Full-size Commercial / Heavy Duty Truck",
    "years_sold_au": {"start": 1948, "end": 2026},
    "locally_built": True,
    "assembly_plants_au": [
        "Broadmeadows, Victoria (F-100/F-250/F-350 assembly until 1992)",
        "Homebush, New South Wales (Assembly 1950s-1970s)",
        "Eagle Farm (Brisbane), Queensland (Truck assembly 1970s-1992)",
        "Mickleham, Victoria (RMA Automotive / Ford Australia factory RHD remanufacturing, 2023-present)",
        "Ipiranga, Brazil (Ford South America RN F-250/F-350 for Ford Australia, 2001-2007)"
    ],
    "overview": "The Ford F-Series is an enduring pillar of Australian outback, farming, and heavy towing history. Locally assembled in Australia across multiple decades in Victoria, New South Wales, and Queensland, Australian F-100s, F-250s, and F-350s were specifically tailored for harsh Aussie work, utilizing local 250ci Falcon straight-sixes, 300ci big sixes, and Geelong-cast 302ci and 351ci Cleveland V8s. In 2001, Ford Australia officially returned to the heavy-duty market with the mighty RN-series F-250 and F-350, powered by the thunderous 7.3L Navistar Power Stroke Turbo Diesel V8 (175 kW / 684 Nm), creating a cult legend among caravan haulers. In 2023, Ford Australia officially launched the Next-Gen F-150 in Australia, remanufactured to OEM right-hand drive in Mickleham, Victoria featuring the 298 kW 3.5L EcoBoost twin-turbo V6 and 4.5-tonne towing capacity.",
    "australian_market_notes": "Australian-assembled F-100s and F-250s featured unique 'Ambulance' high-output alternators, dual fuel tanks, heavy-duty Dana axles, and Australian-built Cleveland V8 engines manufactured at Geelong. The 2001-2007 RN F-250 with the 7.3L Power Stroke V8 became an instant legend, with second-hand examples frequently selling for higher than their original retail prices two decades later.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "Sixth-Seventh-Gen-AU",
            "generation_name": "Sixth & Seventh Gen F-100 / F-250 (Australian Assembly)",
            "years": {"start": 1973, "end": 1992},
            "body_styles": ["Single Cab Styleside Ute", "Single Cab Flareside", "Cab Chassis", "SuperCab"],
            "platform": "Ford F-Series full-perimeter truck chassis",
            "ancap_rating": None,
            "summary": "Assembled in Broadmeadows and Eagle Farm. Twin I-Beam front suspension, fitted with Geelong-cast 302 and 351 Cleveland V8s and 4.1L Falcon straight-six.",
            "engines": [
                {
                    "engine_code": "Cleveland-351-V8-Truck",
                    "name": "Ford Cleveland 351ci (5.8L) OHV V8",
                    "displacement_cc": 5766,
                    "displacement_litres": 5.8,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 150.0,
                    "power_rpm": "4000",
                    "torque_nm": 390.0,
                    "torque_rpm": "2200",
                    "compression_ratio": "8.9:1",
                    "valvetrain": "OHV 16V",
                    "notes": "Geelong-manufactured Cleveland V8 with truck camshaft and heavy-duty cooling."
                },
                {
                    "engine_code": "Ford-300-Big-Six",
                    "name": "Ford 300ci (4.9L) OHV Inline-6",
                    "displacement_cc": 4917,
                    "displacement_litres": 4.9,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 89.0,
                    "power_rpm": "3400",
                    "torque_nm": 320.0,
                    "torque_rpm": "1600",
                    "compression_ratio": "8.0:1",
                    "valvetrain": "OHV 12V",
                    "notes": "Legendary commercial high-torque 7-bearing straight-six."
                }
            ],
            "badges": [
                {
                    "badge_name": "F-100 XLT Styleside",
                    "years": {"start": 1977, "end": 1985},
                    "body_styles": ["Single Cab"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual floor", "3-speed automatic C6"],
                    "msrp_aud_min": 7890,
                    "msrp_aud_max": 11500,
                    "fuel_consumption_l_100km": 17.5,
                    "kerb_weight_kg": 1820,
                    "standard_features": [
                        "351ci Cleveland V8",
                        "Twin I-Beam independent front suspension",
                        "Power steering and front power disc brakes",
                        "Full-length bodyside chrome mouldings and tailgate applique",
                        "Vinyl bench seat with cloth inserts"
                    ],
                    "notes": "Classic Australian outback hauler."
                }
            ],
            "configurations": [
                {
                    "badge_name": "F-100 XLT Styleside",
                    "body_style": "Single Cab",
                    "engine_code": "Cleveland-351-V8-Truck",
                    "transmission": "3-speed automatic C6",
                    "drivetrain": "RWD",
                    "msrp_aud": 8990,
                    "power_kw": 150.0,
                    "torque_nm": 390.0,
                    "fuel_l_100km": 17.5,
                    "towing_braked_kg": 2500,
                    "notes": "Geelong 351 Cleveland V8 Australian F-100."
                }
            ]
        },
        {
            "series_code": "RN-Super-Duty",
            "generation_name": "RN F-250 / F-350 Super Duty",
            "years": {"start": 2001, "end": 2007},
            "body_styles": ["Single Cab", "SuperCab", "Crew Cab"],
            "platform": "Ford Super Duty platform",
            "ancap_rating": None,
            "summary": "Official Ford Australia import. Monumental 7.3L Navistar Power Stroke Turbo Diesel V8 (684 Nm), Dana 60 solid front axle, 4.5-tonne towing, and cavernous dual-cab interior.",
            "engines": [
                {
                    "engine_code": "PowerStroke-7.3-V8",
                    "name": "Ford / Navistar 7.3L Power Stroke Turbo Diesel V8",
                    "displacement_cc": 7274,
                    "displacement_litres": 7.3,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Diesel",
                    "power_kw": 175.0,
                    "power_rpm": "2600",
                    "torque_nm": 684.0,
                    "torque_rpm": "1600",
                    "compression_ratio": "17.5:1",
                    "valvetrain": "OHV 16V",
                    "notes": "HEUI electronic hydraulic direct injection; legendary heavy-towing engine."
                }
            ],
            "badges": [
                {
                    "badge_name": "F-250 XLT Crew Cab 4x4",
                    "years": {"start": 2001, "end": 2007},
                    "body_styles": ["Crew Cab"],
                    "drivetrain": "4WD",
                    "transmissions": ["5-speed manual ZF", "4-speed automatic 4R100"],
                    "msrp_aud_min": 69990,
                    "msrp_aud_max": 76990,
                    "fuel_consumption_l_100km": 14.5,
                    "kerb_weight_kg": 2840,
                    "standard_features": [
                        "7.3L Power Stroke Turbo Diesel V8",
                        "Shift-on-the-fly 4WD with manual lock front hubs",
                        "Heavy-duty solid front and rear axles with leaf springs",
                        "Air conditioning, power windows, and cruise control",
                        "4,500 kg towing capacity"
                    ],
                    "notes": "Cult outback and caravan towing legend."
                }
            ],
            "configurations": [
                {
                    "badge_name": "F-250 XLT Crew Cab 4x4",
                    "body_style": "Crew Cab",
                    "engine_code": "PowerStroke-7.3-V8",
                    "transmission": "4-speed automatic 4R100",
                    "drivetrain": "4WD",
                    "msrp_aud": 74990,
                    "power_kw": 175.0,
                    "torque_nm": 684.0,
                    "fuel_l_100km": 14.5,
                    "towing_braked_kg": 4500,
                    "notes": "7.3L Power Stroke turbo-diesel 4.5-tonne tow champion."
                }
            ]
        },
        {
            "series_code": "Fourteenth-Gen-AU",
            "generation_name": "Fourteenth Gen F-150 (Australian RHD)",
            "years": {"start": 2023, "end": 2026},
            "body_styles": ["Crew Cab (SuperCrew)"],
            "platform": "Ford F-150 high-strength military-grade aluminium alloy platform",
            "ancap_rating": None,
            "summary": "Official Ford Australia factory-backed RHD remanufacturing program by RMA Automotive in Mickleham, Victoria. Powered by 298 kW 3.5L EcoBoost twin-turbo V6 with 4.5-tonne towing.",
            "engines": [
                {
                    "engine_code": "EcoBoost-3.5-TwinTurbo",
                    "name": "Ford EcoBoost 3.5L Twin-Turbo DOHC 24V V6",
                    "displacement_cc": 3497,
                    "displacement_litres": 3.5,
                    "cylinders": 6,
                    "configuration": "V",
                    "aspiration": "Twin-Turbocharged",
                    "fuel_type": "Petrol",
                    "power_kw": 298.0,
                    "power_rpm": "6000",
                    "torque_nm": 678.0,
                    "torque_rpm": "3100",
                    "compression_ratio": "10.5:1",
                    "valvetrain": "DOHC 24V Ti-VCT",
                    "notes": "Twin Garrett turbochargers, direct and port fuel injection; 10-speed auto."
                }
            ],
            "badges": [
                {
                    "badge_name": "F-150 Lariat SuperCrew 4x4",
                    "years": {"start": 2023, "end": 2026},
                    "body_styles": ["Crew Cab"],
                    "drivetrain": "4WD",
                    "transmissions": ["10-speed automatic with SelectShift"],
                    "msrp_aud_min": 139990,
                    "msrp_aud_max": 140945,
                    "fuel_consumption_l_100km": 12.5,
                    "kerb_weight_kg": 2535,
                    "standard_features": [
                        "298 kW / 678 Nm 3.5L Twin-Turbo EcoBoost V6",
                        "High-strength military-grade aluminium alloy body",
                        "12-inch digital instrument cluster and 12-inch SYNC 4 touchscreen",
                        "B&O Unleashed 18-speaker audio system",
                        "Heated and ventilated leather front seats",
                        "Pro Power Onboard generator and 4,500 kg towing capacity"
                    ],
                    "notes": "Flagship Australian-remanufactured luxury truck."
                }
            ],
            "configurations": [
                {
                    "badge_name": "F-150 Lariat SuperCrew 4x4",
                    "body_style": "Crew Cab",
                    "engine_code": "EcoBoost-3.5-TwinTurbo",
                    "transmission": "10-speed automatic with SelectShift",
                    "drivetrain": "4WD",
                    "msrp_aud": 139990,
                    "power_kw": 298.0,
                    "torque_nm": 678.0,
                    "fuel_l_100km": 12.5,
                    "towing_braked_kg": 4500,
                    "notes": "298 kW twin-turbo V6 luxury 4.5-tonne tow truck."
                }
            ]
        }
    ]
}

"""Wave 2 Honda, Suzuki, and Isuzu deep-dive models: Civic, Jimny/Sierra, D-MAX."""

CIVIC_MODEL = {
    "make_slug": "honda",
    "model_slug": "civic",
    "name": "Civic & Civic Type R",
    "vehicle_type": "Hatchback / Sedan",
    "segment": "Small Car / Hot Hatch",
    "years_sold_au": {"start": 1973, "end": "Present"},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Honda Civic is an undisputed benchmark of global and Australian automotive engineering. Spanning eleven generations over more than 50 years, the Civic conquered Australian hearts during the 1970s oil crisis with its revolutionary CVCC clean-burn engine, democratized Formula 1-derived VTEC variable valve timing in the 1990s VTi-R, and evolved into front-wheel-drive circuit royalty with the ferocious Civic Type R.",
    "australian_market_notes": "First sold in Australia in 1973, the first-generation Civic was praised for revolutionary space packaging and front-wheel drive agility. In the 1990s, the EG and EK Civic became tuner royalty with double-wishbone suspension and the screaming 8,200rpm B16A2 VTi-R. In modern times, the British-built FN2, FK8, and Japanese-built FL5 Civic Type R have repeatedly set front-wheel drive lap records at Mount Panorama Bathurst and the Nürburgring Nordschleife.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "1st & 2nd Gen",
            "generation_name": "Civic 1st & 2nd Generation",
            "years": {"start": 1973, "end": 1983},
            "body_styles": ["3-door Hatch", "4-door Sedan", "5-door Station Wagon"],
            "platform": "Honda SB1/SL",
            "ancap_rating": "Untested",
            "summary": "1970s economy champion that established Honda as an automotive power in Australia. Introduced CVCC (Compound Vortex Controlled Combustion) clean-burn engine meeting strict emissions without a catalytic converter.",
            "engines": [
                {
                    "engine_code": "EB1",
                    "name": "Honda EB1 1.2L OHC",
                    "displacement_cc": 1169,
                    "displacement_litres": 1.2,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 37.0,
                    "power_rpm": "5500",
                    "torque_nm": 79.0,
                    "torque_rpm": "3000",
                    "compression_ratio": "8.6:1",
                    "valvetrain": "SOHC 8-valve",
                    "notes": "Lightweight alloy cylinder head transverse engine."
                },
                {
                    "engine_code": "ED1-CVCC",
                    "name": "Honda ED1 1.5L CVCC",
                    "displacement_cc": 1488,
                    "displacement_litres": 1.5,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 46.0,
                    "power_rpm": "5500",
                    "torque_nm": 95.0,
                    "torque_rpm": "3500",
                    "compression_ratio": "8.1:1",
                    "valvetrain": "SOHC 12-valve CVCC",
                    "notes": "Pioneering pre-chamber stratified charge combustion."
                }
            ],
            "badges": [
                {
                    "badge_name": "Civic Hatch / Sedan / Wagon",
                    "years": {"start": 1973, "end": 1983},
                    "body_styles": ["Hatch", "Sedan", "Wagon"],
                    "drivetrain": "FWD",
                    "transmissions": ["4-speed manual", "5-speed manual", "2-speed Hondamatic"],
                    "msrp_aud_min": 2199,
                    "msrp_aud_max": 5490,
                    "fuel_consumption_l_100km": 6.8,
                    "kerb_weight_kg": 680,
                    "standard_features": ["Four-wheel independent MacPherson strut suspension", "Front disc brakes", "Transverse front-wheel drive", "Reclining vinyl bucket seats"],
                    "notes": "Revolutionary light runabout weighing under 700kg."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Civic 1200 Hatch",
                    "body_style": "3-door Hatch",
                    "engine_code": "EB1",
                    "transmission": "4-speed manual",
                    "drivetrain": "FWD",
                    "years_start": 1973,
                    "years_end": 1979,
                    "msrp_aud": 2199,
                    "power_kw": 37.0,
                    "torque_nm": 79.0,
                    "fuel_l_100km": 6.8,
                    "towing_braked_kg": 450,
                    "notes": "The original fuel-crisis game changer."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "3rd & 4th Gen",
            "generation_name": "Civic 3rd & 4th Generation (ED/EF)",
            "years": {"start": 1983, "end": 1991},
            "body_styles": ["3-door Hatch", "4-door Sedan", "Shuttle Wagon", "CRX Coupe"],
            "platform": "Honda AH / ED",
            "ancap_rating": "Untested",
            "summary": "1984 Wheels Car of the Year (Civic Shuttle/CRX). 4th-gen introduced racecar-like double wishbone suspension at all four corners, flush aero styling, and Twin Cam D16 engines in the Si.",
            "engines": [
                {
                    "engine_code": "D16A8",
                    "name": "Honda D16A8 1.6L Twin Cam",
                    "displacement_cc": 1590,
                    "displacement_litres": 1.6,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 96.0,
                    "power_rpm": "6800",
                    "torque_nm": 144.0,
                    "torque_rpm": "5700",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "DOHC 16-valve PGM-FI",
                    "notes": "Free-revving twin-cam in Civic Si and CRX."
                }
            ],
            "badges": [
                {
                    "badge_name": "GL / Breeze / Si",
                    "years": {"start": 1987, "end": 1991},
                    "body_styles": ["3-door Hatch", "4-door Sedan", "Shuttle"],
                    "drivetrain": "FWD (or Real-Time 4WD on Shuttle)",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 14990,
                    "msrp_aud_max": 24990,
                    "fuel_consumption_l_100km": 7.5,
                    "kerb_weight_kg": 940,
                    "standard_features": ["Four-wheel double wishbone suspension", "PGM-FI electronic fuel injection", "Low bonnet line", "Sports seats (Si)"],
                    "notes": "Superb handling chassis."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Civic Si Hatch Manual",
                    "body_style": "3-door Hatch",
                    "engine_code": "D16A8",
                    "transmission": "5-speed manual",
                    "drivetrain": "FWD",
                    "years_start": 1988,
                    "years_end": 1991,
                    "msrp_aud": 22490,
                    "power_kw": 96.0,
                    "torque_nm": 144.0,
                    "fuel_l_100km": 7.5,
                    "towing_braked_kg": 700,
                    "notes": "96kW twin-cam with four-wheel double wishbones."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "5th Gen (EG)",
            "generation_name": "Civic 5th Generation (inc. VTi)",
            "years": {"start": 1991, "end": 1995},
            "body_styles": ["3-door Hatch", "4-door Sedan"],
            "platform": "Honda EG",
            "ancap_rating": "Untested",
            "summary": "Timeless curved styling, split two-piece rear tailgate hatch, and the introduction of VTEC variable valve timing in the Civic VTi (1.6L D16Y1 SOHC VTEC 96kW).",
            "engines": [
                {
                    "engine_code": "D16Y1",
                    "name": "Honda D16Y1 1.6L SOHC VTEC",
                    "displacement_cc": 1590,
                    "displacement_litres": 1.6,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 96.0,
                    "power_rpm": "6600",
                    "torque_nm": 145.0,
                    "torque_rpm": "5200",
                    "compression_ratio": "9.3:1",
                    "valvetrain": "SOHC 16-valve VTEC",
                    "notes": "VTEC cam switch at 4,800rpm."
                }
            ],
            "badges": [
                {
                    "badge_name": "Breeze / GL / GLi",
                    "years": {"start": 1991, "end": 1995},
                    "body_styles": ["3-door Hatch", "4-door Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 16990,
                    "msrp_aud_max": 23990,
                    "fuel_consumption_l_100km": 7.2,
                    "kerb_weight_kg": 985,
                    "standard_features": ["Split tailgate", "Double wishbone suspension", "Power steering", "Air conditioning option"],
                    "notes": "Cult tuner chassis worldwide."
                },
                {
                    "badge_name": "VTi",
                    "years": {"start": 1993, "end": 1995},
                    "body_styles": ["3-door Hatch", "4-door Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 25990,
                    "msrp_aud_max": 28990,
                    "fuel_consumption_l_100km": 7.4,
                    "kerb_weight_kg": 1030,
                    "standard_features": ["VTEC engine", "Four-wheel disc brakes", "Rear spoiler", "Alloy wheels", "Power windows and sunroof", "Sports seats"],
                    "notes": "First VTEC Civic in Australia."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Civic VTi Hatch Manual",
                    "body_style": "3-door Hatch",
                    "engine_code": "D16Y1",
                    "transmission": "5-speed manual",
                    "drivetrain": "FWD",
                    "years_start": 1993,
                    "years_end": 1995,
                    "msrp_aud": 25990,
                    "power_kw": 96.0,
                    "torque_nm": 145.0,
                    "fuel_l_100km": 7.4,
                    "towing_braked_kg": 800,
                    "notes": "VTEC performance hatch icon."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "6th Gen (EK)",
            "generation_name": "Civic 6th Generation & VTi-R",
            "years": {"start": 1995, "end": 2000},
            "body_styles": ["3-door Hatch", "4-door Sedan", "2-door Coupe"],
            "platform": "Honda EK",
            "ancap_rating": "3 stars",
            "summary": "Spawned the legendary Civic VTi-R (EK4) with the 118kW 1.6L B16A2 DOHC VTEC screamer revving to 8,200rpm with double-wishbone suspension.",
            "engines": [
                {
                    "engine_code": "B16A2",
                    "name": "Honda B16A2 1.6L DOHC VTEC",
                    "displacement_cc": 1595,
                    "displacement_litres": 1.6,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Premium Unleaded Petrol",
                    "power_kw": 118.0,
                    "power_rpm": "7600",
                    "torque_nm": 148.0,
                    "torque_rpm": "7000",
                    "compression_ratio": "10.2:1",
                    "valvetrain": "DOHC 16-valve VTEC",
                    "notes": "Producing nearly 100hp per litre naturally aspirated; 8,200rpm redline, VTEC cam switch at 5,700rpm."
                }
            ],
            "badges": [
                {
                    "badge_name": "CXi / GLi",
                    "years": {"start": 1995, "end": 2000},
                    "body_styles": ["3-door Hatch", "4-door Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 19990,
                    "msrp_aud_max": 25990,
                    "fuel_consumption_l_100km": 7.1,
                    "kerb_weight_kg": 1040,
                    "standard_features": ["Double wishbone suspension", "Dual airbags", "Power steering", "Air conditioning"],
                    "notes": "Mainstay Australian small car."
                },
                {
                    "badge_name": "VTi-R (EK4)",
                    "years": {"start": 1996, "end": 2000},
                    "body_styles": ["3-door Hatch"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed close-ratio manual"],
                    "msrp_aud_min": 32990,
                    "msrp_aud_max": 34990,
                    "fuel_consumption_l_100km": 7.9,
                    "kerb_weight_kg": 1090,
                    "standard_features": ["118kW B16A2 DOHC VTEC engine", "15-inch alloy wheels", "Four-wheel disc brakes with ABS", "Front strut tower brace", "Electric sunroof", "Sports cloth seats with patterned inserts", "Rear spoiler"],
                    "notes": "0-100 km/h in 7.8s; screaming 8,200rpm hot hatch legend."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Civic VTi-R EK4 Manual",
                    "body_style": "3-door Hatch",
                    "engine_code": "B16A2",
                    "transmission": "5-speed manual",
                    "drivetrain": "FWD",
                    "years_start": 1996,
                    "years_end": 2000,
                    "msrp_aud": 32990,
                    "power_kw": 118.0,
                    "torque_nm": 148.0,
                    "fuel_l_100km": 7.9,
                    "towing_braked_kg": 800,
                    "notes": "High-revving 8,200rpm VTEC performance icon."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "7th & 8th Gen (EU/FD/FN)",
            "generation_name": "Civic 7th & 8th Gen (inc. FN2 Type R)",
            "years": {"start": 2000, "end": 2011},
            "body_styles": ["5-door Hatch", "4-door Sedan", "3-door Type R Hatch"],
            "platform": "Honda Global Small / European Architecture",
            "ancap_rating": "5 stars (FN2 / FD facelift)",
            "summary": "8th-gen FD introduced space-age dual-tier digital instrumentation, while the UK-built FN2 Civic Type R introduced Australia to the 148kW 2.0L K20Z4 i-VTEC engine.",
            "engines": [
                {
                    "engine_code": "K20Z4",
                    "name": "Honda K20Z4 2.0L DOHC i-VTEC (Type R)",
                    "displacement_cc": 1998,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Premium Unleaded Petrol",
                    "power_kw": 148.0,
                    "power_rpm": "7800",
                    "torque_nm": 193.0,
                    "torque_rpm": "5600",
                    "compression_ratio": "11.0:1",
                    "valvetrain": "DOHC 16-valve i-VTEC",
                    "notes": "8,000rpm redline, magnesium valve cover, balance shafts removed for rapid rev response."
                }
            ],
            "badges": [
                {
                    "badge_name": "FN2 Civic Type R",
                    "years": {"start": 2007, "end": 2011},
                    "body_styles": ["3-door Hatch"],
                    "drivetrain": "FWD",
                    "transmissions": ["6-speed close-ratio manual"],
                    "msrp_aud_min": 39990,
                    "msrp_aud_max": 41990,
                    "fuel_consumption_l_100km": 9.3,
                    "kerb_weight_kg": 1345,
                    "standard_features": ["148kW i-VTEC engine", "Alcantara red/black Recaro sports bucket seats", "18-inch alloy wheels", "Dual-zone digital cockpit", "Aluminium gear knob", "Drilled pedals"],
                    "notes": "First officially sold Civic Type R in Australia."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Civic Type R FN2",
                    "body_style": "3-door Hatch",
                    "engine_code": "K20Z4",
                    "transmission": "6-speed manual",
                    "drivetrain": "FWD",
                    "years_start": 2007,
                    "years_end": 2011,
                    "msrp_aud": 39990,
                    "power_kw": 148.0,
                    "torque_nm": 193.0,
                    "fuel_l_100km": 9.3,
                    "towing_braked_kg": 0,
                    "notes": "0-100 km/h in 6.6 seconds with 8,000rpm redline."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "9th & 10th Gen (FK8)",
            "generation_name": "Civic 9th & 10th Gen (inc. FK8 Type R)",
            "years": {"start": 2012, "end": "2021"},
            "body_styles": ["5-door Hatch", "4-door Sedan"],
            "platform": "Honda Global Compact Platform",
            "ancap_rating": "5 stars",
            "summary": "10th-gen introduced standard multi-link rear suspension and the record-breaking FK8 Civic Type R: 2.0L VTEC Turbo (228kW/400Nm), dual-axis strut suspension, Brembo brakes, and rev-matching manual.",
            "engines": [
                {
                    "engine_code": "K20C1",
                    "name": "Honda K20C1 2.0L VTEC Turbo",
                    "displacement_cc": 1996,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Mono-Scroll Turbocharged Intercooled",
                    "fuel_type": "Premium Unleaded Petrol",
                    "power_kw": 228.0,
                    "power_rpm": "6500",
                    "torque_nm": 400.0,
                    "torque_rpm": "2500-4500",
                    "compression_ratio": "9.8:1",
                    "valvetrain": "DOHC 16-valve VTEC",
                    "notes": "Direct-injected turbo producing 228kW and 400Nm of torque."
                }
            ],
            "badges": [
                {
                    "badge_name": "FK8 Civic Type R",
                    "years": {"start": 2017, "end": "2021"},
                    "body_styles": ["5-door Hatch"],
                    "drivetrain": "FWD with Helical LSD",
                    "transmissions": ["6-speed manual with rev-matching"],
                    "msrp_aud_min": 50990,
                    "msrp_aud_max": 54990,
                    "fuel_consumption_l_100km": 8.8,
                    "kerb_weight_kg": 1393,
                    "standard_features": ["228kW turbo engine", "Dual-Axis strut front suspension eliminating torque steer", "Adaptive damper system (Comfort/Sport/+R)", "Brembo 4-piston 350mm front brakes", "20-inch alloy wheels with Continental SportContact 6 tyres", "Triple exhaust outlets", "Vortex generators & rear wing"],
                    "notes": "Set production front-wheel-drive lap records at Mount Panorama Bathurst and Nürburgring."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Civic Type R FK8",
                    "body_style": "5-door Hatch",
                    "engine_code": "K20C1",
                    "transmission": "6-speed manual",
                    "drivetrain": "FWD",
                    "years_start": 2017,
                    "years_end": 2021,
                    "msrp_aud": 50990,
                    "power_kw": 228.0,
                    "torque_nm": 400.0,
                    "fuel_l_100km": 8.8,
                    "towing_braked_kg": 0,
                    "notes": "228kW track-destroying hot hatch."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "11th Gen (FL5)",
            "generation_name": "Civic 11th Gen & FL5 Type R",
            "years": {"start": 2021, "end": "Present"},
            "body_styles": ["5-door Hatch"],
            "platform": "Honda Architecture (HA)",
            "ancap_rating": "5 stars (Standard Civic)",
            "summary": "Sophisticated minimalist styling, standard e:HEV hybrid delivering 4.2L/100km, and the pinnacle FL5 Civic Type R delivering 235kW/420Nm with integrated LogR telemetry and widebody arches.",
            "engines": [
                {
                    "engine_code": "K20C1-FL5",
                    "name": "Honda K20C1 2.0L VTEC Turbo (FL5)",
                    "displacement_cc": 1996,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Mono-Scroll Turbocharged Intercooled",
                    "fuel_type": "Premium Unleaded Petrol",
                    "power_kw": 235.0,
                    "power_rpm": "6500",
                    "torque_nm": 420.0,
                    "torque_rpm": "2600-4000",
                    "compression_ratio": "9.8:1",
                    "valvetrain": "DOHC 16-valve VTEC",
                    "notes": "Redesigned turbocharger turbine wheel and housing producing 235kW and 420Nm."
                }
            ],
            "badges": [
                {
                    "badge_name": "e:HEV LX",
                    "years": {"start": 2022, "end": "Present"},
                    "body_styles": ["5-door Hatch"],
                    "drivetrain": "FWD",
                    "transmissions": ["e-CVT electric drive"],
                    "msrp_aud_min": 55000,
                    "msrp_aud_max": 55000,
                    "fuel_consumption_l_100km": 4.2,
                    "kerb_weight_kg": 1475,
                    "standard_features": ["2.0L Atkinson hybrid with 135kW/315Nm", "10.2-inch digital cluster", "9-inch touchscreen", "Bose 12-speaker audio", "Honda SENSING suite"],
                    "notes": "4.2L/100km combined economy."
                },
                {
                    "badge_name": "FL5 Civic Type R",
                    "years": {"start": 2023, "end": "Present"},
                    "body_styles": ["5-door Hatch"],
                    "drivetrain": "FWD with Helical LSD",
                    "transmissions": ["6-speed close-ratio manual with rev-match"],
                    "msrp_aud_min": 72600,
                    "msrp_aud_max": 72600,
                    "fuel_consumption_l_100km": 8.9,
                    "kerb_weight_kg": 1429,
                    "standard_features": ["235kW/420Nm turbo engine", "Integrated widebody fenders stamped from factory", "19-inch reverse-rim lightweight alloys with Michelin Pilot Sport 4S tyres", "Die-cast aluminium rear spoiler stanchions", "Red Alcantara bucket seats and red carpeting", "Honda LogR real-time track telemetry app"],
                    "notes": "Suzuka and Nürburgring FWD record holder; sold out in Australia."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Civic Type R FL5",
                    "body_style": "5-door Hatch",
                    "engine_code": "K20C1-FL5",
                    "transmission": "6-speed manual",
                    "drivetrain": "FWD",
                    "years_start": 2023,
                    "years_end": "Present",
                    "msrp_aud": 72600,
                    "power_kw": 235.0,
                    "torque_nm": 420.0,
                    "fuel_l_100km": 8.9,
                    "towing_braked_kg": 0,
                    "notes": "235kW / 420Nm benchmark front-drive track car; 0-100 km/h in 5.4 seconds."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

JIMNY_SIERRA_MODEL = {
    "make_slug": "suzuki",
    "model_slug": "jimny-sierra",
    "name": "Jimny / Sierra / Stockman",
    "vehicle_type": "Compact 4WD SUV",
    "segment": "Light 4WD",
    "years_sold_au": {"start": 1974, "end": "Present"},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Suzuki Jimny, Sierra, and Stockman represent Australia's most revered lightweight, go-anywhere 4WD institution. Defying its miniature dimensions with a genuine ladder-frame chassis, dual-range transfer case, and live beam axles front and rear, it has conquered the Simpson Desert, Victorian High Country, and outback cattle stations for half a century.",
    "australian_market_notes": "First imported in 1974 as the two-stroke LJ50 and four-stroke LJ80 Stockman, it became an agricultural essential on Aussie farms. In 1981, the SJ410 and SJ413 Sierra ignited a 4WD craze among Australian youth, delivering unbeatable rock-crawling capability for a fraction of the cost of a LandCruiser. The 1998 JB33/JB43 introduced coil springs, while the 2018 JB74 retro styling sparked unprecedented multi-year Australian dealer waitlists, expanded in 2024 with the 5-door Jimny XL.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "LJ50/LJ80",
            "generation_name": "LJ50 & LJ80 (Stockman / Brute)",
            "years": {"start": 1974, "end": 1981},
            "body_styles": ["Soft-top Canvas", "Hardtop Metal-roof", "Cab Chassis Tray Ute"],
            "platform": "Suzuki LJ",
            "ancap_rating": "Untested",
            "summary": "The pioneer. LJ50 (539cc 3-cylinder 2-stroke water-cooled), followed by LJ80 (797cc 4-stroke 4-cylinder), ladder-frame chassis, live leaf-sprung axles, and sub-700kg weight.",
            "engines": [
                {
                    "engine_code": "LJ50-2T",
                    "name": "Suzuki 539cc 3-Cylinder 2-Stroke",
                    "displacement_cc": 539,
                    "displacement_litres": 0.5,
                    "cylinders": 3,
                    "configuration": "Inline-3 (2-Stroke)",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol (Pre-mix)",
                    "power_kw": 25.0,
                    "power_rpm": "4500",
                    "torque_nm": 52.0,
                    "torque_rpm": "3000",
                    "compression_ratio": "6.8:1",
                    "valvetrain": "Piston Port 2-Stroke",
                    "notes": "Water-cooled 3-cylinder two-stroke engine in early Australian LJ50s."
                },
                {
                    "engine_code": "F8A",
                    "name": "Suzuki F8A 797cc 4-Stroke",
                    "displacement_cc": 797,
                    "displacement_litres": 0.8,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 31.0,
                    "power_rpm": "5500",
                    "torque_nm": 60.0,
                    "torque_rpm": "3500",
                    "compression_ratio": "8.7:1",
                    "valvetrain": "SOHC 8-valve",
                    "notes": "Suzuki's first 4-stroke automotive engine fitted to LJ80."
                }
            ],
            "badges": [
                {
                    "badge_name": "Stockman / Brute",
                    "years": {"start": 1974, "end": 1981},
                    "body_styles": ["Canvas Soft Top", "Metal Top", "Cab Chassis Ute"],
                    "drivetrain": "Part-Time 4WD with low-range transfer case",
                    "transmissions": ["4-speed manual"],
                    "msrp_aud_min": 1995,
                    "msrp_aud_max": 3495,
                    "fuel_consumption_l_100km": 7.8,
                    "kerb_weight_kg": 670,
                    "standard_features": ["Ladder chassis", "Live axles with leaf springs front and rear", "Dual-range transfer case", "Canvas doors (removable)", "Fold-down windscreen"],
                    "notes": "Pioneering bush runabout."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Suzuki LJ80 Stockman",
                    "body_style": "Soft-top Canvas",
                    "engine_code": "F8A",
                    "transmission": "4-speed manual",
                    "drivetrain": "4WD",
                    "years_start": 1978,
                    "years_end": 1981,
                    "msrp_aud": 2995,
                    "power_kw": 31.0,
                    "torque_nm": 60.0,
                    "fuel_l_100km": 7.8,
                    "towing_braked_kg": 450,
                    "notes": "Featherweight 4-stroke outback legend."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "SJ410/SJ413",
            "generation_name": "Sierra (SJ Series)",
            "years": {"start": 1981, "end": 1998},
            "body_styles": ["Soft-top Canvas", "Hardtop Van", "Long Wheelbase Tray Ute (Stockman)"],
            "platform": "Suzuki SJ",
            "ancap_rating": "Untested",
            "summary": "17-year reign that defined affordable 4WD culture in Australia. SJ410 (1.0L F10A) and SJ413 (1.3L G13A), wide-track updates, and coil-sprung Samurai.",
            "engines": [
                {
                    "engine_code": "G13A / G13BA",
                    "name": "Suzuki G13 1.3L OHC",
                    "displacement_cc": 1324,
                    "displacement_litres": 1.3,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 47.0,
                    "power_rpm": "5300",
                    "torque_nm": 100.0,
                    "torque_rpm": "3000",
                    "compression_ratio": "8.9:1",
                    "valvetrain": "SOHC 8-valve",
                    "notes": "Fitted to SJ413 and wide-track Sierra."
                }
            ],
            "badges": [
                {
                    "badge_name": "Sierra Soft Top & Hardtop",
                    "years": {"start": 1981, "end": 1998},
                    "body_styles": ["Soft-top", "Hardtop"],
                    "drivetrain": "Part-Time 4WD with low range",
                    "transmissions": ["4-speed manual", "5-speed manual"],
                    "msrp_aud_min": 6990,
                    "msrp_aud_max": 16990,
                    "fuel_consumption_l_100km": 8.5,
                    "kerb_weight_kg": 890,
                    "standard_features": ["Dual-range transfer case", "Manual freewheeling front hubs", "Front disc brakes (SJ413)", "Roll bar", "Fold-down windscreen"],
                    "notes": "Unstoppable rock crawler and budget 4x4 icon."
                },
                {
                    "badge_name": "Sierra Stockman Tray Ute",
                    "years": {"start": 1982, "end": 1998},
                    "body_styles": ["Long Wheelbase Cab Chassis Tray"],
                    "drivetrain": "Part-Time 4WD with low range",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 8990,
                    "msrp_aud_max": 17990,
                    "fuel_consumption_l_100km": 8.9,
                    "kerb_weight_kg": 950,
                    "standard_features": ["Long wheelbase chassis", "Dropside aluminium or steel tray", "Heavy-duty rear leaf springs", "Vinyl interior"],
                    "notes": "Australian agricultural workhorse."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Suzuki Sierra Soft Top 1.3",
                    "body_style": "Soft-top Canvas",
                    "engine_code": "G13A / G13BA",
                    "transmission": "5-speed manual",
                    "drivetrain": "4WD",
                    "years_start": 1988,
                    "years_end": 1996,
                    "msrp_aud": 12990,
                    "power_kw": 47.0,
                    "torque_nm": 100.0,
                    "fuel_l_100km": 8.5,
                    "towing_braked_kg": 750,
                    "notes": "Wide-track Australian Sierra."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "JB33/JB43",
            "generation_name": "Jimny 3rd Generation",
            "years": {"start": 1998, "end": 2018},
            "body_styles": ["3-door Hardtop SUV"],
            "platform": "Suzuki JB",
            "ancap_rating": "3 stars",
            "summary": "20-year production lifespan. Introduced aerodynamic rounded styling, coil-sprung 3-link rigid live axles front and rear, push-button electronic 4WD, and 1.3L M13A engine.",
            "engines": [
                {
                    "engine_code": "M13A",
                    "name": "Suzuki M13A 1.3L DOHC VVT",
                    "displacement_cc": 1328,
                    "displacement_litres": 1.3,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 63.0,
                    "power_rpm": "6000",
                    "torque_nm": 110.0,
                    "torque_rpm": "4100",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "DOHC 16-valve VVT",
                    "notes": "Aluminium twin-cam engine with variable valve timing from 2005."
                }
            ],
            "badges": [
                {
                    "badge_name": "JLX / Sierra",
                    "years": {"start": 1998, "end": 2018},
                    "body_styles": ["3-door SUV"],
                    "drivetrain": "Drive Action 4x4 with low range",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 16990,
                    "msrp_aud_max": 22990,
                    "fuel_consumption_l_100km": 7.3,
                    "kerb_weight_kg": 1060,
                    "standard_features": ["Coil-sprung live axles front & rear", "Push-button low-range 4WD", "Dual front airbags", "Air conditioning", "Roof rails", "15-inch alloys"],
                    "notes": "Beloved compact mountain goat."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Jimny Sierra Manual",
                    "body_style": "3-door Hardtop SUV",
                    "engine_code": "M13A",
                    "transmission": "5-speed manual",
                    "drivetrain": "4WD",
                    "years_start": 2005,
                    "years_end": 2018,
                    "msrp_aud": 19990,
                    "power_kw": 63.0,
                    "torque_nm": 110.0,
                    "fuel_l_100km": 7.3,
                    "towing_braked_kg": 950,
                    "notes": "Coil-sprung solid axles front and rear."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "JB64/JB74",
            "generation_name": "Jimny 4th Gen & 5-Door XL",
            "years": {"start": 2018, "end": "Present"},
            "body_styles": ["3-door SUV", "5-door SUV (Jimny XL)"],
            "platform": "Suzuki JB74",
            "ancap_rating": "3 stars",
            "summary": "Sensational retro boxy styling that created nationwide multi-year waiting lists. Features 1.5L K15B engine, AllGrip Pro 4WD with low-range transfer lever, and the 340mm longer 5-door Jimny XL launched in 2024.",
            "engines": [
                {
                    "engine_code": "K15B",
                    "name": "Suzuki K15B 1.5L DOHC VVT",
                    "displacement_cc": 1462,
                    "displacement_litres": 1.5,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 75.0,
                    "power_rpm": "6000",
                    "torque_nm": 130.0,
                    "torque_rpm": "4000",
                    "compression_ratio": "10.0:1",
                    "valvetrain": "DOHC 16-valve VVT",
                    "notes": "Lightweight 1.5L engine matched to mechanical transfer case."
                }
            ],
            "badges": [
                {
                    "badge_name": "Lite / GLX (3-Door)",
                    "years": {"start": 2018, "end": "Present"},
                    "body_styles": ["3-door SUV"],
                    "drivetrain": "AllGrip Pro part-time 4WD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 25990,
                    "msrp_aud_max": 33490,
                    "fuel_consumption_l_100km": 6.4,
                    "kerb_weight_kg": 1095,
                    "standard_features": ["Ladder chassis with X-member bracing", "3-link rigid live axles with coil springs", "Autonomous emergency braking & lane departure warning", "LED projector headlamps (GLX)", "7-inch touchscreen with Apple CarPlay (GLX)"],
                    "notes": "Australian cult vehicle with extreme resale values."
                },
                {
                    "badge_name": "Jimny XL (5-Door)",
                    "years": {"start": 2024, "end": "Present"},
                    "body_styles": ["5-door SUV"],
                    "drivetrain": "AllGrip Pro part-time 4WD",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 34990,
                    "msrp_aud_max": 36490,
                    "fuel_consumption_l_100km": 6.9,
                    "kerb_weight_kg": 1185,
                    "standard_features": ["340mm longer wheelbase", "5 full passenger doors", "9.0-inch touchscreen infotainment", "Wireless Apple CarPlay", "Dual camera brake support", "211 litres luggage capacity"],
                    "notes": "Long-awaited 5-door practical adventure model."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Jimny GLX 3-door Manual",
                    "body_style": "3-door SUV",
                    "engine_code": "K15B",
                    "transmission": "5-speed manual",
                    "drivetrain": "4WD",
                    "years_start": 2018,
                    "years_end": "Present",
                    "msrp_aud": 28490,
                    "power_kw": 75.0,
                    "torque_nm": 130.0,
                    "fuel_l_100km": 6.4,
                    "towing_braked_kg": 1300,
                    "notes": "Cult hero off-roader with 37-degree approach angle."
                },
                {
                    "badge_name": "Jimny XL 5-door Auto",
                    "body_style": "5-door SUV",
                    "engine_code": "K15B",
                    "transmission": "4-speed automatic",
                    "drivetrain": "4WD",
                    "years_start": 2024,
                    "years_end": "Present",
                    "msrp_aud": 36490,
                    "power_kw": 75.0,
                    "torque_nm": 130.0,
                    "fuel_l_100km": 6.9,
                    "towing_braked_kg": 1300,
                    "notes": "5-door practical variant launched in 2024."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

ISUZU_DMAX_MODEL = {
    "make_slug": "isuzu",
    "model_slug": "d-max",
    "name": "D-MAX",
    "vehicle_type": "Ute / Cab Chassis",
    "segment": "Light Commercial",
    "years_sold_au": {"start": 2008, "end": "Present"},
    "locally_built": False,
    "assembly_plants_au": [],
    "overview": "The Isuzu D-MAX is an Australian commercial and recreational ute powerhouse. Renowned for its commercial truck-derived 3.0-litre 4JJ-series turbo diesel engine, 3,500kg braked towing capacity, and unbreakable durability, the D-MAX grew from an independent newcomer in 2008 into the third best-selling vehicle outright in Australia.",
    "australian_market_notes": "Launched in late 2008 following the separation of Isuzu from the General Motors-Holden Rodeo joint venture, Isuzu UTE Australia established itself as an independent force. The D-MAX won fierce loyalty among caravanners, grey nomads, tradies, and outback tourers due to the under-stressed, gear-and-chain driven 4JJ1 engine. In 2020, the RG generation revolutionized ute safety by introducing the full IDAS safety suite and a centre airbag, earning a 5-star ANCAP rating across every single cab and chassis derivative, topped by the Walkinshaw-engineered Blade flagship in 2024.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "RA/RC",
            "generation_name": "D-MAX 1st Generation",
            "years": {"start": 2008, "end": 2012},
            "body_styles": ["Single Cab", "Space Cab", "Crew Cab"],
            "platform": "Isuzu TF",
            "ancap_rating": "3 stars",
            "summary": "Inaugural standalone model from Isuzu Ute Australia. Featured the commercial-grade 3.0L 4JJ1-TC turbo diesel (120kW/360Nm) with steel timing gears and dual-range 4WD.",
            "engines": [
                {
                    "engine_code": "4JJ1-TC",
                    "name": "Isuzu 4JJ1-TC 3.0L Turbo Diesel",
                    "displacement_cc": 2999,
                    "displacement_litres": 3.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 120.0,
                    "power_rpm": "3600",
                    "torque_nm": 360.0,
                    "torque_rpm": "1800",
                    "compression_ratio": "17.5:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Commercial truck-derived engine with split gear camshaft drive and roller rocker arms."
                }
            ],
            "badges": [
                {
                    "badge_name": "SX / LS / LS-U",
                    "years": {"start": 2008, "end": 2012},
                    "body_styles": ["Single Cab", "Space Cab", "Crew Cab"],
                    "drivetrain": "4x2 or 4x4",
                    "transmissions": ["5-speed manual", "4-speed automatic"],
                    "msrp_aud_min": 23990,
                    "msrp_aud_max": 42500,
                    "fuel_consumption_l_100km": 8.4,
                    "kerb_weight_kg": 1850,
                    "standard_features": ["3,000kg braked towing capacity", "Push-button 4WD shift-on-the-fly", "Dual airbags", "ABS brakes", "16-inch alloy wheels (LS-U)"],
                    "notes": "Formed Isuzu's reputation for bulletproof reliability."
                }
            ],
            "configurations": [
                {
                    "badge_name": "D-MAX LS-U 4x4 Crew Cab",
                    "body_style": "Crew Cab",
                    "engine_code": "4JJ1-TC",
                    "transmission": "5-speed manual",
                    "drivetrain": "4WD",
                    "years_start": 2008,
                    "years_end": 2012,
                    "msrp_aud": 41490,
                    "power_kw": 120.0,
                    "torque_nm": 360.0,
                    "fuel_l_100km": 8.4,
                    "towing_braked_kg": 3000,
                    "notes": "Original independent Isuzu Ute launch vehicle."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "RT50/RT85",
            "generation_name": "D-MAX 2nd Generation",
            "years": {"start": 2012, "end": 2020},
            "body_styles": ["Single Cab", "Space Cab", "Crew Cab"],
            "platform": "Isuzu RT",
            "ancap_rating": "5 stars (facelift)",
            "summary": "Modernized styling, class-leading 3,500kg braked towing capacity, and the legendary Euro 5 4JJ1-TCX engine upgrade in 2017 boasting 130kW/430Nm and 6-speed Aisin automatic.",
            "engines": [
                {
                    "engine_code": "4JJ1-TCX",
                    "name": "Isuzu 4JJ1-TCX 3.0L Hi-Power Turbo Diesel",
                    "displacement_cc": 2999,
                    "displacement_litres": 3.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Variable Geometry Turbocharged Intercooled (VGS)",
                    "fuel_type": "Diesel",
                    "power_kw": 130.0,
                    "power_rpm": "3600",
                    "torque_nm": 430.0,
                    "torque_rpm": "2000-2200",
                    "compression_ratio": "16.3:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Re-engineered for Euro 5 emissions in 2017 with variable-geometry turbo and 430Nm torque."
                }
            ],
            "badges": [
                {
                    "badge_name": "SX / LS-M",
                    "years": {"start": 2012, "end": 2020},
                    "body_styles": ["Single Cab", "Space Cab", "Crew Cab"],
                    "drivetrain": "4x2 or 4x4",
                    "transmissions": ["5-speed manual", "6-speed manual", "5-speed auto", "6-speed auto"],
                    "msrp_aud_min": 27490,
                    "msrp_aud_max": 46990,
                    "fuel_consumption_l_100km": 7.9,
                    "kerb_weight_kg": 1890,
                    "standard_features": ["3,500kg braked towing capacity", "6 airbags standard", "Electronic stability control", "Vinyl or cloth flooring", "Rear step bumper"],
                    "notes": "Workhorse of outback fleets and contractors."
                },
                {
                    "badge_name": "LS-U / LS-T / X-Runner",
                    "years": {"start": 2012, "end": 2020},
                    "body_styles": ["Space Cab", "Crew Cab"],
                    "drivetrain": "4x2 or 4x4",
                    "transmissions": ["6-speed manual", "6-speed automatic"],
                    "msrp_aud_min": 44490,
                    "msrp_aud_max": 54990,
                    "fuel_consumption_l_100km": 7.9,
                    "kerb_weight_kg": 1945,
                    "standard_features": ["17 or 18-inch alloy wheels", "Leather seats (LS-T)", "Touchscreen with sat nav", "Side steps", "Reversing camera", "Projector headlamps with LED DRLs"],
                    "notes": "Caravanner and adventure favourite."
                }
            ],
            "configurations": [
                {
                    "badge_name": "D-MAX LS-U 4x4 Crew Cab Auto",
                    "body_style": "Crew Cab",
                    "engine_code": "4JJ1-TCX",
                    "transmission": "6-speed automatic",
                    "drivetrain": "4WD",
                    "years_start": 2017,
                    "years_end": 2020,
                    "msrp_aud": 48300,
                    "power_kw": 130.0,
                    "torque_nm": 430.0,
                    "fuel_l_100km": 7.9,
                    "towing_braked_kg": 3500,
                    "notes": "3.5-tonne towing workhorse with bulletproof 4JJ1 engine."
                }
            ],
            "manuals": [],
            "pictures": []
        },
        {
            "series_code": "RG01",
            "generation_name": "D-MAX 3rd Gen & Blade",
            "years": {"start": 2020, "end": "Present"},
            "body_styles": ["Single Cab", "Space Cab", "Crew Cab"],
            "platform": "Isuzu RG",
            "ancap_rating": "5 stars",
            "summary": "Reset commercial ute standards. First ute to achieve 5-star ANCAP under strict 2020 protocols with standard front centre airbag and IDAS stereo-camera safety across the entire range. Powered by the upgraded 140kW/450Nm 4JJ3-TCX, rear diff lock, and flagship Walkinshaw-developed Blade off-road edition.",
            "engines": [
                {
                    "engine_code": "4JJ3-TCX",
                    "name": "Isuzu 4JJ3-TCX 3.0L Turbo Diesel",
                    "displacement_cc": 2999,
                    "displacement_litres": 3.0,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Variable Geometry Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 140.0,
                    "power_rpm": "3600",
                    "torque_nm": 450.0,
                    "torque_rpm": "1600-2600",
                    "compression_ratio": "16.3:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "Upgraded with electronically controlled VGS turbo, 250MPa high-pressure common rail, and cast alloy pistons; 450Nm broad torque curve."
                },
                {
                    "engine_code": "RZ4E-TC",
                    "name": "Isuzu RZ4E-TC 1.9L Turbo Diesel",
                    "displacement_cc": 1898,
                    "displacement_litres": 1.9,
                    "cylinders": 4,
                    "configuration": "Inline-4",
                    "aspiration": "Turbocharged Intercooled",
                    "fuel_type": "Diesel",
                    "power_kw": 110.0,
                    "power_rpm": "3600",
                    "torque_nm": 350.0,
                    "torque_rpm": "1800-2600",
                    "compression_ratio": "15.9:1",
                    "valvetrain": "DOHC 16-valve",
                    "notes": "High efficiency 1.9L diesel introduced in entry SX work models in 2022."
                }
            ],
            "badges": [
                {
                    "badge_name": "SX / LS-M",
                    "years": {"start": 2020, "end": "Present"},
                    "body_styles": ["Single Cab", "Space Cab", "Crew Cab"],
                    "drivetrain": "4x2 or 4x4 with rear differential lock",
                    "transmissions": ["6-speed manual", "6-speed automatic"],
                    "msrp_aud_min": 32200,
                    "msrp_aud_max": 53800,
                    "fuel_consumption_l_100km": 7.7,
                    "kerb_weight_kg": 1940,
                    "standard_features": ["IDAS (Intelligent Driver Assistance System) with autonomous emergency braking", "Front centre airbag (8 airbags total)", "Rear differential lock standard on 4x4", "7-inch touchscreen with wireless Apple CarPlay"],
                    "notes": "5-star ANCAP safety standard on every single work ute variant."
                },
                {
                    "badge_name": "LS-U / LS-U+",
                    "years": {"start": 2020, "end": "Present"},
                    "body_styles": ["Space Cab", "Crew Cab"],
                    "drivetrain": "4x2 or 4x4",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 59000,
                    "msrp_aud_max": 63500,
                    "fuel_consumption_l_100km": 8.0,
                    "kerb_weight_kg": 2040,
                    "standard_features": ["9-inch infotainment touchscreen", "Tow bar receiver standard", "Tub liner", "Heated leather seats (LS-U+)", "Dual-zone climate control", "Blind spot monitoring"],
                    "notes": "The touring caravanner sweet spot."
                },
                {
                    "badge_name": "X-Terrain & Blade",
                    "years": {"start": 2020, "end": "Present"},
                    "body_styles": ["Crew Cab"],
                    "drivetrain": "4x4 with rear differential lock",
                    "transmissions": ["6-speed automatic"],
                    "msrp_aud_min": 67500,
                    "msrp_aud_max": 76990,
                    "fuel_consumption_l_100km": 8.0,
                    "kerb_weight_kg": 2175,
                    "standard_features": ["Walkinshaw-engineered MTV dampers (Blade)", "29mm suspension lift with widened track (Blade)", "17-inch flow-formed alloys with Goodyear Wrangler Duratrac tyres (Blade)", "Heavy-duty steel bash plate and recovery points (Blade)", "Electric roller tonneau cover (X-Terrain)", "Aero sports bar", "Remote engine start"],
                    "notes": "Walkinshaw-developed Blade introduced in late 2024 as extreme off-road flagship."
                }
            ],
            "configurations": [
                {
                    "badge_name": "D-MAX X-Terrain 4x4 Auto",
                    "body_style": "Crew Cab",
                    "engine_code": "4JJ3-TCX",
                    "transmission": "6-speed automatic",
                    "drivetrain": "4WD",
                    "years_start": 2020,
                    "years_end": "Present",
                    "msrp_aud": 67500,
                    "power_kw": 140.0,
                    "torque_nm": 450.0,
                    "fuel_l_100km": 8.0,
                    "towing_braked_kg": 3500,
                    "notes": "Flagship dual-cab ute with 3.5t towing and 5-star ANCAP safety."
                },
                {
                    "badge_name": "D-MAX Blade Walkinshaw 4x4",
                    "body_style": "Crew Cab",
                    "engine_code": "4JJ3-TCX",
                    "transmission": "6-speed automatic",
                    "drivetrain": "4WD",
                    "years_start": 2024,
                    "years_end": "Present",
                    "msrp_aud": 76990,
                    "power_kw": 140.0,
                    "torque_nm": 450.0,
                    "fuel_l_100km": 8.0,
                    "towing_braked_kg": 3500,
                    "notes": "Walkinshaw-engineered extreme off-road package with 29mm lift."
                }
            ],
            "manuals": [],
            "pictures": []
        }
    ]
}

"""Catalog data for Toyota, Mazda, Mitsubishi, and Nissan in Australia."""

MAKES_PART1 = [
    {
        "make_slug": "toyota",
        "name": "Toyota",
        "country_of_origin": "Japan",
        "years_active_au": {"start": 1959, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": True,
        "overview": "Australia's perpetual market leader and automotive titan. Toyota began Australian operations in 1958 with LandCruisers on the Snowy Mountains Scheme and assembled vehicles locally at Port Melbourne and Altona from 1963 to 2017.",
        "australian_history": """Toyota's Australian story began in 1958 when civil engineering contractor Leslie Thiess imported 13 FJ25 LandCruisers for use on the rugged construction terrain of the Snowy Mountains Hydro-Electric Scheme. Impressed by their unbreakable mechanical toughness, Thiess secured Queensland distribution rights in 1959, forming Thiess Toyota.

In 1963, Australian Motor Industries (AMI) at Port Melbourne, Victoria negotiated CKD (Complete Knock Down) assembly rights for Toyota passenger cars, making Australia Toyota's very first vehicle manufacturing site outside of Japan. The first vehicle assembled was the Tiara (RT20/RT30), quickly followed by the Corona in 1964, the Crown luxury sedan, and the Corolla (KE10) in 1968.

By the 1970s, Toyota had expanded into full Australian manufacturing. Toyota Motor Corporation Japan gradually acquired shares in AMI, renaming the operation Toyota Motor Corporation Australia (TMCA). Under the Federal Government's Button Car Plan in 1989, Toyota and General Motors-Holden established the United Australian Automotive Industries (UAAI) joint venture. Holden built the Commodore for Toyota to sell as the Toyota Lexcen, while Toyota manufactured the Corolla and Camry for Holden to sell as the Holden Nova and Apollo.

In 1994, Toyota commissioned a brand new, world-class vehicle manufacturing complex at Altona in Melbourne's western suburbs, transitioning Port Melbourne to engine manufacturing and casting. In 2000, Toyota introduced the Altona-built Avalon large sedan, later replaced in 2006 by the 3.5L V6 Aurion alongside the Camry. In 2010, Altona launched Australia's very first locally manufactured hybrid passenger car, the Camry Hybrid (AHV40), unveiled by Prime Minister Kevin Rudd.

Toyota officially overtook Holden and Ford in 2003 to become Australia's overall best-selling automotive brand, a crown it has held without interruption for over two decades. The HiLux utility and RAV4 crossover have repeatedly been Australia's #1 selling individual vehicles. Local car assembly concluded at Altona on October 3, 2017 after 54 years and 3,451,115 vehicles built. Toyota maintains its Australian headquarters, national engineering center, product design studio, and extensive testing grounds at Altona and Anglesea.""",
        "models_catalog": [
            {
                "model_slug": "tiara",
                "name": "Tiara",
                "vehicle_type": "Sedan",
                "segment": "Small Car",
                "years_sold_au": {"start": 1963, "end": 1965},
                "locally_built": True,
                "overview": "The first Toyota assembled in Australia by AMI in Port Melbourne, laying the foundation for Toyota's domestic manufacturing history.",
                "generations": [
                    {"series_code": "RT20", "generation_name": "Tiara 1500 / 1900", "years": {"start": 1963, "end": 1965}, "body_styles": ["Sedan", "Wagon", "Ute"], "summary": "1.5L and 1.9L pushrod 4-cylinder engine, 3-speed manual, CKD assembly at Port Melbourne."}
                ]
            },
            {
                "model_slug": "corona",
                "name": "Corona",
                "vehicle_type": "Sedan / Wagon",
                "segment": "Mid-size Car",
                "years_sold_au": {"start": 1964, "end": 1987},
                "locally_built": True,
                "overview": "Long-running Australian family car assembled in Port Melbourne across multiple generations until succeeded by the Camry.",
                "generations": [
                    {"series_code": "RT40", "generation_name": "Corona 3rd Gen", "years": {"start": 1964, "end": 1970}, "body_styles": ["Sedan", "Wagon", "Ute"], "summary": "Shovel-nose design, 1.5L 2R engine, established Toyota's reputation for build quality."},
                    {"series_code": "RT80", "generation_name": "Corona 4th Gen", "years": {"start": 1970, "end": 1974}, "body_styles": ["Sedan", "Wagon"], "summary": "1.6L 12R engine, improved passenger comfort and local suspension tuning."},
                    {"series_code": "RT104", "generation_name": "Corona 5th Gen", "years": {"start": 1974, "end": 1979}, "body_styles": ["Sedan", "Wagon"], "summary": "1.8L 16R and 2.0L 18R engines, popular company fleet and family vehicle."},
                    {"series_code": "RT132", "generation_name": "Corona 6th Gen", "years": {"start": 1979, "end": 1983}, "body_styles": ["Sedan", "Liftback", "Wagon"], "summary": "Square-edged styling, Holden 1.9L Starfire 4-cylinder fitted to meet local content rules, also 2.0L 18R-C."},
                    {"series_code": "RT142", "generation_name": "Corona 7th Gen (Avante)", "years": {"start": 1983, "end": 1987}, "body_styles": ["Sedan", "Wagon"], "summary": "Last RWD Corona in Australia, 2.4L 22R-E EFI engine on Avante, IRS rear suspension."}
                ]
            },
            {
                "model_slug": "crown",
                "name": "Crown",
                "vehicle_type": "Sedan / Wagon",
                "segment": "Large Luxury Car",
                "years_sold_au": {"start": 1964, "end": 1991},
                "locally_built": True,
                "overview": "Toyota's flagship executive sedan and wagon, assembled locally by AMI until 1980 and then fully imported until 1991.",
                "generations": [
                    {"series_code": "S40", "generation_name": "Crown 2nd Gen", "years": {"start": 1964, "end": 1967}, "body_styles": ["Sedan", "Wagon"], "summary": "First Crown in Australia, 1.9L 3R engine, durable body-on-frame chassis."},
                    {"series_code": "S50", "generation_name": "Crown 3rd Gen", "years": {"start": 1967, "end": 1971}, "body_styles": ["Sedan", "Wagon"], "summary": "2.0L M-series inline-6 introduced, Port Melbourne assembly."},
                    {"series_code": "S60", "generation_name": "Crown 4th Gen 'Whale'", "years": {"start": 1971, "end": 1974}, "body_styles": ["Sedan", "Coupe", "Wagon"], "summary": "Distinctive avant-garde body, 2.3L and 2.6L inline-6 engines."},
                    {"series_code": "S80", "generation_name": "Crown 5th Gen", "years": {"start": 1974, "end": 1979}, "body_styles": ["Sedan", "Wagon"], "summary": "Royal Lounge trim, 2.6L 4M engine, 4-speed automatic options."},
                    {"series_code": "S110", "generation_name": "Crown 6th Gen", "years": {"start": 1979, "end": 1983}, "body_styles": ["Sedan", "Wagon"], "summary": "2.8L 5M-E fuel-injected engine, digital instruments, imported from Japan."},
                    {"series_code": "S120", "generation_name": "Crown 7th Gen", "years": {"start": 1983, "end": 1988}, "body_styles": ["Sedan"], "summary": "Royal Saloon with 2.8L DOHC 5M-GE, TEMS electronic suspension."},
                    {"series_code": "S130", "generation_name": "Crown 8th Gen", "years": {"start": 1988, "end": 1991}, "body_styles": ["Sedan"], "summary": "Final Australian-market Crown, 3.0L 7M-GE inline-6, succeeded by Lexus LS400."}
                ]
            },
            {
                "model_slug": "corolla",
                "name": "Corolla",
                "vehicle_type": "Hatchback / Sedan / Wagon",
                "segment": "Small Car",
                "years_sold_au": {"start": 1967, "end": "Present"},
                "locally_built": True,
                "overview": "Australia's defining small car nameplate, built locally in Victoria from 1968 to 1999 across Port Melbourne, Duncans Road, and Altona.",
                "generations": [
                    {"series_code": "KE10", "generation_name": "Corolla 1st Gen", "years": {"start": 1967, "end": 1970}, "body_styles": ["Sedan", "Wagon"], "summary": "1.1L K engine, local CKD assembly commenced July 1968 at Port Melbourne."},
                    {"series_code": "KE20", "generation_name": "Corolla 2nd Gen", "years": {"start": 1970, "end": 1974}, "body_styles": ["Sedan", "Coupe", "Wagon"], "summary": "1.2L 3K engine, famous 'coke bottle' styling, strong seller."},
                    {"series_code": "KE30/KE55", "generation_name": "Corolla 3rd Gen", "years": {"start": 1974, "end": 1981}, "body_styles": ["Sedan", "Coupe", "Liftback", "Wagon"], "summary": "1.2L 3K and 1.3L 4K engines, SE, CS, and Sport Coupe models."},
                    {"series_code": "KE70/AE71", "generation_name": "Corolla 4th Gen", "years": {"start": 1981, "end": 1985}, "body_styles": ["Sedan", "Wagon", "Panel Van"], "summary": "1.3L 4K-C and 1.6L 4A-C engines, rack and pinion steering, T-18 liftback."},
                    {"series_code": "AE80/AE82/AE86", "generation_name": "Corolla 5th Gen", "years": {"start": 1985, "end": 1989}, "body_styles": ["Hatchback", "Sedan", "Coupe"], "summary": "Switch to FWD, famous 4A-GE Twin Cam in Seca SX; imported RWD AE86 Sprinter 1983-1985."},
                    {"series_code": "AE90/AE92", "generation_name": "Corolla 6th Gen", "years": {"start": 1989, "end": 1994}, "body_styles": ["Hatchback", "Sedan", "Seca"], "summary": "1.4L 6A-FC, 1.6L 4A-FE, and 100kW 4A-GE SX; also sold as Holden Nova."},
                    {"series_code": "AE101/AE102", "generation_name": "Corolla 7th Gen", "years": {"start": 1994, "end": 1999}, "body_styles": ["Hatchback", "Sedan", "Seca"], "summary": "Built at new Altona plant; 1.6L 4A-FE and 1.8L 7A-FE; CSi, Conquest, RV, and Ultima."},
                    {"series_code": "AE112", "generation_name": "Corolla 8th Gen", "years": {"start": 1998, "end": 2001}, "body_styles": ["Hatchback", "Sedan", "Seca Liftback"], "summary": "Last locally built Corolla; 1.8L 7A-FE, Levin, and limited-edition 115kW Turbo Sportivo."},
                    {"series_code": "ZZE122", "generation_name": "Corolla 9th Gen", "years": {"start": 2001, "end": 2007}, "body_styles": ["Hatchback", "Sedan", "Wagon"], "summary": "Fully imported from Japan/South Africa; 1.8L 1ZZ-FE; Sportivo featured 141kW 2ZZ-GE VVTL-i."},
                    {"series_code": "ZRE152", "generation_name": "Corolla 10th Gen", "years": {"start": 2007, "end": 2012}, "body_styles": ["Hatchback", "Sedan"], "summary": "1.8L 2ZR-FE Dual VVT-i 100kW, Ascent, Conquest, Levin SX, and Levin ZR."},
                    {"series_code": "ZRE182/ZWE186", "generation_name": "Corolla 11th Gen", "years": {"start": 2012, "end": 2018}, "body_styles": ["Hatchback", "Sedan"], "summary": "Sharp wedge styling; introduced Corolla Hybrid in 2016 pairing 1.8L with electric motor."},
                    {"series_code": "E210", "generation_name": "Corolla 12th Gen", "years": {"start": 2018, "end": "Present"}, "body_styles": ["Hatchback", "Sedan"], "summary": "TNGA-C platform, 2.0L M20A-FKS petrol, 1.8L Hybrid, and AWD GR Corolla 221kW turbo."}
                ]
            },
            {
                "model_slug": "camry",
                "name": "Camry",
                "vehicle_type": "Sedan / Wagon",
                "segment": "Mid-size Car",
                "years_sold_au": {"start": 1983, "end": "Present"},
                "locally_built": True,
                "overview": "The cornerstone of Australian automotive manufacturing from 1987 to 2017, built in Altona and Port Melbourne and Australia's #1 mid-size car for over 30 years.",
                "generations": [
                    {"series_code": "SV11", "generation_name": "Camry 1st Gen", "years": {"start": 1983, "end": 1987}, "body_styles": ["Sedan", "Liftback"], "summary": "Imported liftback and sedan with 2.0L 2S-C engine, establishing Camry nametag in Australia."},
                    {"series_code": "SV21", "generation_name": "Camry 2nd Gen", "years": {"start": 1987, "end": 1993}, "body_styles": ["Sedan", "Wagon"], "summary": "First Australian-built Camry at Port Melbourne; 2.0L 3S-FE; CS, CSX, Ultima; rebadged as Holden Apollo."},
                    {"series_code": "SDV10/SXV10", "generation_name": "Camry 3rd Gen (Widebody)", "years": {"start": 1993, "end": 1997}, "body_styles": ["Sedan", "Wagon"], "summary": "Altona production started; 2.2L 5S-FE 4-cylinder and 3.0L 3VZ-FE V6 (Camry Vienta)."},
                    {"series_code": "SXV20/MCV20", "generation_name": "Camry 4th Gen", "years": {"start": 1997, "end": 2002}, "body_styles": ["Sedan", "Wagon"], "summary": "Major export earner to the Middle East; 2.2L 5S-FE and 3.0L 1MZ-FE V6; Touring and Azura."},
                    {"series_code": "ACV36/MCV36", "generation_name": "Camry 5th Gen", "years": {"start": 2002, "end": 2006}, "body_styles": ["Sedan"], "summary": "2.4L 2AZ-FE VVTi and 3.0L 1MZ-FE V6; Altise, Ateva, Sportivo, and Azura grades."},
                    {"series_code": "ACV40/AHV40", "generation_name": "Camry 6th Gen", "years": {"start": 2006, "end": 2011}, "body_styles": ["Sedan"], "summary": "2.4L 2AZ-FE; 2010 launched Australia's first locally built hybrid passenger car (Camry Hybrid)."},
                    {"series_code": "ASV50/AVV50", "generation_name": "Camry 7th Gen", "years": {"start": 2011, "end": 2017}, "body_styles": ["Sedan"], "summary": "2.5L 2AR-FE and 2AR-FXE Hybrid; Altise, Atara S/SX/SL; final vehicle off Altona line 3 Oct 2017."},
                    {"series_code": "AXVH70/GSV70", "generation_name": "Camry 8th Gen", "years": {"start": 2017, "end": 2024}, "body_styles": ["Sedan"], "summary": "Imported on TNGA-K platform; 2.5L Hybrid, 2.5L petrol, and 224kW 3.5L V6 (Ascent, SX, SL)."},
                    {"series_code": "XV80", "generation_name": "Camry 9th Gen", "years": {"start": 2024, "end": "Present"}, "body_styles": ["Sedan"], "summary": "Hybrid-only range featuring 5th-gen Toyota Hybrid System with 2.5L 4-cylinder."}
                ]
            },
            {
                "model_slug": "aurion",
                "name": "Aurion",
                "vehicle_type": "Sedan",
                "segment": "Large Car",
                "years_sold_au": {"start": 2006, "end": 2017},
                "locally_built": True,
                "overview": "Australian-designed and built large front-wheel-drive sedan, powered exclusively by the 3.5L 2GR-FE V6 and built at Altona.",
                "generations": [
                    {"series_code": "GSV40", "generation_name": "Aurion 1st Gen", "years": {"start": 2006, "end": 2012}, "body_styles": ["Sedan"], "summary": "3.5L 2GR-FE 200kW V6; AT-X, Touring, Sportivo, Prodigy, Presara; TRD supercharged 241kW model in 2007."},
                    {"series_code": "GSV50", "generation_name": "Aurion 2nd Gen", "years": {"start": 2012, "end": 2017}, "body_styles": ["Sedan"], "summary": "Refined 3.5L V6 200kW, 6-speed auto, built at Altona until plant closure in 2017."}
                ]
            },
            {
                "model_slug": "avalon",
                "name": "Avalon",
                "vehicle_type": "Sedan",
                "segment": "Large Car",
                "years_sold_au": {"start": 2000, "end": 2005},
                "locally_built": True,
                "overview": "Spacious family and taxi sedan built at Altona to take on Holden Commodore and Ford Falcon.",
                "generations": [
                    {"series_code": "MCX10", "generation_name": "Avalon Mark I & II", "years": {"start": 2000, "end": 2005}, "body_styles": ["Sedan"], "summary": "3.0L 1MZ-FE V6, Conquest, CSX, Grande, and sporty Advantage models; Altona assembly."}
                ]
            },
            {
                "model_slug": "celica",
                "name": "Celica",
                "vehicle_type": "Coupe / Liftback",
                "segment": "Sports Car",
                "years_sold_au": {"start": 1971, "end": 2005},
                "locally_built": False,
                "overview": "Toyota's iconic sports coupe in Australia, from classic 1970s rear-drive models to AWD turbo GT-Four rally weapons.",
                "generations": [
                    {"series_code": "TA22/RA23", "generation_name": "Celica 1st Gen", "years": {"start": 1971, "end": 1977}, "body_styles": ["Coupe", "Liftback"], "summary": "1.6L 2T-G and 2.0L 18R engines, Australian motorsport cult classic."},
                    {"series_code": "RA40", "generation_name": "Celica 2nd Gen", "years": {"start": 1977, "end": 1981}, "body_styles": ["Coupe", "Liftback"], "summary": "2.0L 18R-C, round then square headlights, LT and XT trims."},
                    {"series_code": "RA60/RA65", "generation_name": "Celica 3rd Gen", "years": {"start": 1981, "end": 1985}, "body_styles": ["Coupe", "Liftback"], "summary": "Pop-up lights, 2.0L 21R-C and 2.4L 22R-E EFI, IRS rear suspension."},
                    {"series_code": "ST162", "generation_name": "Celica 4th Gen", "years": {"start": 1985, "end": 1989}, "body_styles": ["Coupe", "Liftback"], "summary": "Transition to FWD, 2.0L 3S-GE DOHC 103kW engine; SX trim."},
                    {"series_code": "ST184/ST185", "generation_name": "Celica 5th Gen", "years": {"start": 1989, "end": 1993}, "body_styles": ["Liftback", "Coupe"], "summary": "Curvaceous styling, 2.2L 5S-FE, and world rally champion GT-Four turbo AWD (ST185)."},
                    {"series_code": "ST204/ST205", "generation_name": "Celica 6th Gen", "years": {"start": 1993, "end": 1999}, "body_styles": ["Liftback", "Coupe"], "summary": "Quad round headlights, 2.2L 5S-FE, and limited Group A Rallye GT-Four (ST205)."},
                    {"series_code": "ZZT231", "generation_name": "Celica 7th Gen", "years": {"start": 1999, "end": 2005}, "body_styles": ["Liftback"], "summary": "High-revving 1.8L 2ZZ-GE VVTL-i 140kW engine, 6-speed manual, SX and ZR grades."}
                ]
            },
            {
                "model_slug": "supra",
                "name": "Supra",
                "vehicle_type": "Coupe",
                "segment": "Sports Car",
                "years_sold_au": {"start": 1983, "end": "Present"},
                "locally_built": False,
                "overview": "Toyota's flagship high-performance sports car, from the Celica Supra MA61 through the twin-turbo 2JZ A80 to the modern GR Supra.",
                "generations": [
                    {"series_code": "MA61", "generation_name": "Celica Supra (A60)", "years": {"start": 1983, "end": 1986}, "body_styles": ["Liftback Coupe"], "summary": "2.8L 5M-E and DOHC 5M-GE inline-6, flared wheelarches, pop-up lights."},
                    {"series_code": "MA70", "generation_name": "Supra 3rd Gen (A70)", "years": {"start": 1986, "end": 1992}, "body_styles": ["Liftback Coupe", "Targa"], "summary": "3.0L 7M-GE and 7M-GTE Turbo (173kW), TEMS electronic dampers, digital dash."},
                    {"series_code": "JZA80", "generation_name": "Supra 4th Gen (A80)", "years": {"start": 1993, "end": 1996}, "body_styles": ["Coupe", "Targa"], "summary": "Legendary 2JZ-GTE 3.0L Twin-Turbo 243kW, 6-speed Getrag manual, active aero spoiler."},
                    {"series_code": "DB/A90", "generation_name": "GR Supra 5th Gen (A90)", "years": {"start": 2019, "end": "Present"}, "body_styles": ["Coupe"], "summary": "BMW B58 3.0L Turbo inline-6 (250kW-285kW), 8-speed auto and 6-speed manual; GT and GTS."}
                ]
            },
            {
                "model_slug": "mr2",
                "name": "MR2",
                "vehicle_type": "Coupe / Roadster",
                "segment": "Sports Car",
                "years_sold_au": {"start": 1987, "end": 2005},
                "locally_built": False,
                "overview": "Mid-engine, rear-wheel-drive sports car celebrated for razor-sharp handling across three distinct generations.",
                "generations": [
                    {"series_code": "AW11", "generation_name": "MR2 1st Gen", "years": {"start": 1987, "end": 1989}, "body_styles": ["Coupe", "T-Bar"], "summary": "Mid-mounted 1.6L 4A-GE Twin Cam, Lotus-assisted suspension tuning, wedge styling."},
                    {"series_code": "SW20", "generation_name": "MR2 2nd Gen", "years": {"start": 1990, "end": 1999}, "body_styles": ["Coupe", "T-Bar"], "summary": "2.0L 3S-GE naturally aspirated (Bathurst trim) and imported 3S-GTE turbo models."},
                    {"series_code": "ZZW30", "generation_name": "MR2 Spyder 3rd Gen", "years": {"start": 2000, "end": 2005}, "body_styles": ["Roadster Convertible"], "summary": "Lightweight 975kg roadster with mid-mounted 1.8L 1ZZ-FE engine and sequential manual."}
                ]
            },
            {
                "model_slug": "paseo",
                "name": "Paseo",
                "vehicle_type": "Coupe",
                "segment": "Small Sports Car",
                "years_sold_au": {"start": 1991, "end": 1999},
                "locally_built": False,
                "overview": "Compact, affordable coupe based on the Starlet/Tercel platform.",
                "generations": [
                    {"series_code": "EL44", "generation_name": "Paseo 1st Gen", "years": {"start": 1991, "end": 1995}, "body_styles": ["Coupe"], "summary": "1.5L 5E-FE 74kW engine, front-wheel drive, sporty budget transport."},
                    {"series_code": "EL54", "generation_name": "Paseo 2nd Gen", "years": {"start": 1995, "end": 1999}, "body_styles": ["Coupe"], "summary": "Refreshed aerodynamic styling, 1.5L 5E-FE with improved torque delivery."}
                ]
            },
            {
                "model_slug": "starlet",
                "name": "Starlet",
                "vehicle_type": "Hatchback",
                "segment": "Light Car",
                "years_sold_au": {"start": 1996, "end": 1999},
                "locally_built": False,
                "overview": "Toyota's entry-level light hatchback in Australia prior to the arrival of the Echo.",
                "generations": [
                    {"series_code": "EP91", "generation_name": "Starlet 5th Gen", "years": {"start": 1996, "end": 1999}, "body_styles": ["3-door Hatch", "5-door Hatch"], "summary": "1.3L 4E-FE 55kW engine; Life, Group, and Style trims."}
                ]
            },
            {
                "model_slug": "echo",
                "name": "Echo",
                "vehicle_type": "Hatchback / Sedan",
                "segment": "Light Car",
                "years_sold_au": {"start": 1999, "end": 2005},
                "locally_built": False,
                "overview": "Innovative, space-efficient light car with central digital dashboard, a runaway sales hit.",
                "generations": [
                    {"series_code": "NCP10/NCP12", "generation_name": "Echo 1st Gen", "years": {"start": 1999, "end": 2005}, "body_styles": ["3-door Hatch", "5-door Hatch", "4-door Sedan"], "summary": "1.3L 2NZ-FE and 1.5L 1NZ-FE (Sportivo) VVT-i engines, upright spacious packaging."}
                ]
            },
            {
                "model_slug": "yaris",
                "name": "Yaris",
                "vehicle_type": "Hatchback / Sedan",
                "segment": "Light Car",
                "years_sold_au": {"start": 2005, "end": "Present"},
                "locally_built": False,
                "overview": "Successor to the Echo and a cornerstone of the Australian light car market, including the rally-bred GR Yaris.",
                "generations": [
                    {"series_code": "XP90", "generation_name": "Yaris 1st Gen (AU)", "years": {"start": 2005, "end": 2011}, "body_styles": ["3-door Hatch", "5-door Hatch", "Sedan"], "summary": "1.3L 2NZ-FE and 1.5L 1NZ-FE; YR, YRS, and YRX trims."},
                    {"series_code": "XP130", "generation_name": "Yaris 2nd Gen (AU)", "years": {"start": 2011, "end": 2020}, "body_styles": ["5-door Hatch", "Sedan"], "summary": "Sharp modern styling, 1.3L and 1.5L engines; Ascent, SX, and ZR grades."},
                    {"series_code": "XP210", "generation_name": "Yaris 3rd Gen (AU)", "years": {"start": 2020, "end": "Present"}, "body_styles": ["5-door Hatch"], "summary": "TNGA-B platform, 1.5L 3-cylinder M15A-FKS petrol and hybrid; GR Yaris 200kW/370Nm AWD."}
                ]
            },
            {
                "model_slug": "yaris-cross",
                "name": "Yaris Cross",
                "vehicle_type": "SUV",
                "segment": "Light SUV",
                "years_sold_au": {"start": 2020, "end": "Present"},
                "locally_built": False,
                "overview": "Subcompact high-riding crossover on the TNGA-B platform, highly popular for fuel-sipping hybrid variants.",
                "generations": [
                    {"series_code": "XP210-SUV", "generation_name": "Yaris Cross 1st Gen", "years": {"start": 2020, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "1.5L 3-cylinder petrol and hybrid 2WD/AWD; GX, GXL, Urban, and GR Sport."}
                ]
            },
            {
                "model_slug": "prius",
                "name": "Prius",
                "vehicle_type": "Liftback / Sedan",
                "segment": "Small / Medium Hybrid",
                "years_sold_au": {"start": 2001, "end": 2022},
                "locally_built": False,
                "overview": "The pioneer of petrol-electric hybrid motoring in Australia, transforming environmental awareness across fleets and private buyers.",
                "generations": [
                    {"series_code": "NHW11", "generation_name": "Prius 1st Gen", "years": {"start": 2001, "end": 2003}, "body_styles": ["Sedan"], "summary": "1.5L 1NZ-FXE with Toyota Hybrid System, Australia's first mass-market hybrid car."},
                    {"series_code": "NHW20", "generation_name": "Prius 2nd Gen", "years": {"start": 2003, "end": 2009}, "body_styles": ["Liftback"], "summary": "Iconic aerodynamic kammback liftback silhouette, 1.5L THS-II hybrid, 4.4L/100km."},
                    {"series_code": "ZVW30", "generation_name": "Prius 3rd Gen", "years": {"start": 2009, "end": 2015}, "body_styles": ["Liftback"], "summary": "1.8L 2ZR-FXE Atkinson-cycle hybrid, solar roof panel option, 3.9L/100km."},
                    {"series_code": "ZVW50", "generation_name": "Prius 4th Gen", "years": {"start": 2016, "end": 2022}, "body_styles": ["Liftback"], "summary": "TNGA-K platform, independent rear suspension, 3.4L/100km fuel economy."}
                ]
            },
            {
                "model_slug": "c-hr",
                "name": "C-HR",
                "vehicle_type": "SUV",
                "segment": "Small SUV",
                "years_sold_au": {"start": 2017, "end": "Present"},
                "locally_built": False,
                "overview": "Distinctively styled coupe-crossover offering agile TNGA handling and turbo/hybrid drivetrains.",
                "generations": [
                    {"series_code": "AX10", "generation_name": "C-HR 1st Gen", "years": {"start": 2017, "end": 2023}, "body_styles": ["5-door SUV"], "summary": "1.2L turbo 8NR-FTS and 1.8L 2ZR-FXE hybrid; GXL, Koba, and GR Sport grades."},
                    {"series_code": "AX20", "generation_name": "C-HR 2nd Gen", "years": {"start": 2024, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "European-designed hybrid-only model, 1.8L and 2.0L AWD hybrid powertrains."}
                ]
            },
            {
                "model_slug": "corolla-cross",
                "name": "Corolla Cross",
                "vehicle_type": "SUV",
                "segment": "Small SUV",
                "years_sold_au": {"start": 2022, "end": "Present"},
                "locally_built": False,
                "overview": "Practical compact SUV slotting between Yaris Cross and RAV4, featuring 5th-generation hybrid technology.",
                "generations": [
                    {"series_code": "XG10", "generation_name": "Corolla Cross 1st Gen", "years": {"start": 2022, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "2.0L M20A-FKS petrol and 2.0L 5th-gen Hybrid with E-Four AWD; GX, GXL, Atmos."}
                ]
            },
            {
                "model_slug": "rav4",
                "name": "RAV4",
                "vehicle_type": "SUV",
                "segment": "Medium SUV",
                "years_sold_au": {"start": 1994, "end": "Present"},
                "locally_built": False,
                "overview": "The pioneer of the monocoque lifestyle SUV market in 1994, now one of Australia's highest-selling passenger vehicles.",
                "generations": [
                    {"series_code": "XA10", "generation_name": "RAV4 1st Gen", "years": {"start": 1994, "end": 2000}, "body_styles": ["3-door SUV", "5-door SUV"], "summary": "2.0L 3S-FE engine, monocoque chassis with full-time AWD, fun city-to-beach runabout."},
                    {"series_code": "XA20", "generation_name": "RAV4 2nd Gen", "years": {"start": 2000, "end": 2006}, "body_styles": ["3-door SUV", "5-door SUV"], "summary": "2.0L 1AZ-FE and 2.4L 2AZ-FE VVTi engines; Edge, Cruiser, and Extreme grades."},
                    {"series_code": "XA30", "generation_name": "RAV4 3rd Gen", "years": {"start": 2006, "end": 2012}, "body_styles": ["5-door SUV"], "summary": "2.4L 4-cylinder and powerful 201kW 3.5L 2GR-FE V6 (CV6, SX6, ZR6)."},
                    {"series_code": "XA40", "generation_name": "RAV4 4th Gen", "years": {"start": 2012, "end": 2019}, "body_styles": ["5-door SUV"], "summary": "2.0L petrol 2WD, 2.5L petrol AWD, and 2.2L turbo-diesel; GX, GXL, Cruiser."},
                    {"series_code": "XA50", "generation_name": "RAV4 5th Gen", "years": {"start": 2019, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "TNGA-K platform, runaway market success with 2.5L Hybrid e-Four; GX, GXL, Cruiser, Edge."}
                ]
            },
            {
                "model_slug": "kluger",
                "name": "Kluger",
                "vehicle_type": "SUV",
                "segment": "Large SUV",
                "years_sold_au": {"start": 2003, "end": "Present"},
                "locally_built": False,
                "overview": "Spacious 7-seat family crossover that became Australia's premier car-like family SUV alternative to Ford Territory and Holden Commodore wagons.",
                "generations": [
                    {"series_code": "MCU28", "generation_name": "Kluger 1st Gen", "years": {"start": 2003, "end": 2007}, "body_styles": ["5-door SUV"], "summary": "3.3L 3MZ-FE V6, full-time AWD, CV, CVX, and Grande models."},
                    {"series_code": "GSU40/45", "generation_name": "Kluger 2nd Gen", "years": {"start": 2007, "end": 2014}, "body_styles": ["5-door SUV"], "summary": "3.5L 2GR-FE 201kW V6, 2WD and AWD, KX-R, KX-S, and Grande."},
                    {"series_code": "GSU50/55", "generation_name": "Kluger 3rd Gen", "years": {"start": 2014, "end": 2021}, "body_styles": ["5-door SUV"], "summary": "Built in Indiana, USA for Australia; 3.5L direct-injected V6, GX, GXL, Grande."},
                    {"series_code": "GSU60/AXUH78", "generation_name": "Kluger 4th Gen", "years": {"start": 2021, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "TNGA-K platform, introduces 2.5L Hybrid AWD alongside 2.4L turbo petrol."}
                ]
            },
            {
                "model_slug": "fortuner",
                "name": "Fortuner",
                "vehicle_type": "SUV",
                "segment": "Large 4WD SUV",
                "years_sold_au": {"start": 2015, "end": "Present"},
                "locally_built": False,
                "overview": "Rugged 7-seat 4WD wagon built on the HiLux ladder chassis with coil-spring rear suspension.",
                "generations": [
                    {"series_code": "AN160", "generation_name": "Fortuner 1st Gen (AU)", "years": {"start": 2015, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "2.8L 1GD-FTV turbo-diesel (130kW-150kW), dual-range 4WD, GX, GXL, Crusade."}
                ]
            },
            {
                "model_slug": "prado",
                "name": "LandCruiser Prado",
                "vehicle_type": "SUV",
                "segment": "Large 4WD SUV",
                "years_sold_au": {"start": 1996, "end": "Present"},
                "locally_built": False,
                "overview": "Australia's favourite long-range outback touring 4WD, pairing dual fuel tanks and heavy towing capability with daily comfort.",
                "generations": [
                    {"series_code": "90 Series", "generation_name": "Prado 90 Series", "years": {"start": 1996, "end": 2002}, "body_styles": ["3-door Wagon", "5-door Wagon"], "summary": "3.4L 5VZ-FE V6 and 3.0L 1KZ-TE turbo-diesel; RV, GXL, TX, Grande."},
                    {"series_code": "120 Series", "generation_name": "Prado 120 Series", "years": {"start": 2003, "end": 2009}, "body_styles": ["5-door Wagon"], "summary": "4.0L 1GR-FE V6 and 3.0L 1KD-FTV D-4D diesel, 180-litre fuel capacity; GX, GXL, VX, Grande."},
                    {"series_code": "150 Series", "generation_name": "Prado 150 Series", "years": {"start": 2009, "end": 2024}, "body_styles": ["3-door Wagon", "5-door Wagon"], "summary": "3.0L 1KD-FTV then 2.8L 1GD-FTV diesel, KDSS suspension; GX, GXL, VX, Kakadu."},
                    {"series_code": "250 Series", "generation_name": "Prado 250 Series", "years": {"start": 2024, "end": "Present"}, "body_styles": ["5-door Wagon"], "summary": "TNGA-F platform, 2.8L 1GD-FTV 48V V-Active mild hybrid, 8-speed automatic."}
                ]
            },
            {
                "model_slug": "landcruiser",
                "name": "LandCruiser",
                "vehicle_type": "4WD / Wagon / Cab Chassis",
                "segment": "Upper Large 4WD",
                "years_sold_au": {"start": 1958, "end": "Present"},
                "locally_built": False,
                "overview": "The undisputed King of the Australian Outback, an indelible part of national infrastructure, agriculture, mining, and remote exploration.",
                "generations": [
                    {"series_code": "40 Series", "generation_name": "LandCruiser 40 Series", "years": {"start": 1960, "end": 1984}, "body_styles": ["SWB Soft/Hardtop", "Troop Carrier", "Cab Chassis"], "summary": "F, 2F petrol and B, 2H diesel engines; FJ40, FJ45, BJ42, HJ47; Snowy Mountains legend."},
                    {"series_code": "55 Series", "generation_name": "LandCruiser 55 Series", "years": {"start": 1969, "end": 1980}, "body_styles": ["Station Wagon"], "summary": "'Iron Pig' wagon, 3.9L F and 4.2L 2F inline-6 petrol engines, first dedicated comfort wagon."},
                    {"series_code": "60 Series", "generation_name": "LandCruiser 60 Series", "years": {"start": 1980, "end": 1990}, "body_styles": ["Station Wagon"], "summary": "2H 4.0L diesel, 12H-T turbo-diesel, 2F/3F petrol; introduced Sahara luxury grade."},
                    {"series_code": "70 Series", "generation_name": "LandCruiser 70 Series", "years": {"start": 1984, "end": "Present"}, "body_styles": ["Single Cab", "Double Cab", "Troop Carrier", "Wagon"], "summary": "Heavy-duty icon: HZJ75, HDJ79, VDJ79 4.5L V8 turbo-diesel, and 2024 GDJ79 2.8L 4-cyl."},
                    {"series_code": "80 Series", "generation_name": "LandCruiser 80 Series", "years": {"start": 1990, "end": 1998}, "body_styles": ["Station Wagon"], "summary": "All-coil suspension revolution; 1HZ 4.2L diesel, 1HD-T turbo-diesel, 1FZ-FE 4.5L twin-cam; GXL, Sahara."},
                    {"series_code": "100/105 Series", "generation_name": "LandCruiser 100/105 Series", "years": {"start": 1998, "end": 2007}, "body_styles": ["Station Wagon"], "summary": "IFS 100 series (4.7L 2UZ-FE V8, 4.2L 1HD-FTE turbo-diesel) and live-axle 105 series (1HZ, 1FZ-FE)."},
                    {"series_code": "200 Series", "generation_name": "LandCruiser 200 Series", "years": {"start": 2007, "end": 2021}, "body_styles": ["Station Wagon"], "summary": "4.5L 1VD-FTV Twin-Turbo V8 diesel (200kW/650Nm) and 4.6L/4.7L petrol V8; GX, GXL, VX, Sahara."},
                    {"series_code": "300 Series", "generation_name": "LandCruiser 300 Series", "years": {"start": 2021, "end": "Present"}, "body_styles": ["Station Wagon"], "summary": "TNGA-F platform, 3.3L F33A-FTV Twin-Turbo V6 diesel 227kW/700Nm, 10-speed auto; GR Sport, Sahara ZX."}
                ]
            },
            {
                "model_slug": "fj-cruiser",
                "name": "FJ Cruiser",
                "vehicle_type": "SUV",
                "segment": "Large 4WD SUV",
                "years_sold_au": {"start": 2011, "end": 2016},
                "locally_built": False,
                "overview": "Retro-styled homage to the iconic FJ40 LandCruiser, featuring suicide rear doors and serious off-road capability.",
                "generations": [
                    {"series_code": "GSJ15", "generation_name": "FJ Cruiser", "years": {"start": 2011, "end": 2016}, "body_styles": ["5-door SUV (Suicide doors)"], "summary": "4.0L 1GR-FE V6 200kW, part-time 4WD, rear differential lock, active traction control."}
                ]
            },
            {
                "model_slug": "hilux",
                "name": "HiLux",
                "vehicle_type": "Ute / Cab Chassis",
                "segment": "Light Commercial",
                "years_sold_au": {"start": 1968, "end": "Present"},
                "locally_built": False,
                "overview": "Australia's top-selling vehicle for seven consecutive years, an unstoppable workhorse from job sites to remote stations.",
                "generations": [
                    {"series_code": "RN10", "generation_name": "HiLux 1st Gen", "years": {"start": 1968, "end": 1972}, "body_styles": ["Single Cab Ute"], "summary": "1.5L 2R engine, 4-speed column shift, payload capacity 1 ton."},
                    {"series_code": "RN20", "generation_name": "HiLux 2nd Gen", "years": {"start": 1972, "end": 1978}, "body_styles": ["Single Cab Ute"], "summary": "1.6L 12R and 2.0L 18R engines, longer cargo bed options."},
                    {"series_code": "RN30/LN40", "generation_name": "HiLux 3rd Gen", "years": {"start": 1978, "end": 1983}, "body_styles": ["Single Cab", "Dual Cab"], "summary": "Introduced factory 4WD and 2.2L L-series diesel engine; pioneer of the family dual-cab ute."},
                    {"series_code": "LN65/YN65", "generation_name": "HiLux 4th Gen", "years": {"start": 1983, "end": 1988}, "body_styles": ["Single Cab", "Xtra Cab", "Dual Cab"], "summary": "Solid beam axles front and rear, 2.4L 2L diesel and 4Y petrol engines; rugged legend."},
                    {"series_code": "LN106/RN105", "generation_name": "HiLux 5th Gen", "years": {"start": 1988, "end": 1997}, "body_styles": ["Single Cab", "Xtra Cab", "Dual Cab"], "summary": "2.8L 3L diesel and 2.4L 22R petrol, leaf-sprung beam axles, unbreakable reputation."},
                    {"series_code": "KZN165/RZN149", "generation_name": "HiLux 6th Gen", "years": {"start": 1997, "end": 2005}, "body_styles": ["Single Cab", "Xtra Cab", "Dual Cab"], "summary": "IFS front suspension, 3.0L 1KZ-TE turbo-diesel and 3.4L 5VZ-FE V6; SR5 badge established."},
                    {"series_code": "KUN26/GGN25", "generation_name": "HiLux 7th Gen", "years": {"start": 2005, "end": 2015}, "body_styles": ["Single Cab", "Extra Cab", "Double Cab"], "summary": "3.0L 1KD-FTV D-4D common-rail diesel and 4.0L 1GR-FE V6; TRD supercharged 225kW model."},
                    {"series_code": "N80/GUN126", "generation_name": "HiLux 8th Gen", "years": {"start": 2015, "end": "Present"}, "body_styles": ["Single Cab", "Extra Cab", "Double Cab"], "summary": "2.8L 1GD-FTV turbo-diesel, WorkMate, SR, SR5, Rogue, Rugged X, and wide-track GR Sport."}
                ]
            },
            {
                "model_slug": "stout",
                "name": "Stout",
                "vehicle_type": "Ute / Light Truck",
                "segment": "Light Commercial",
                "years_sold_au": {"start": 1964, "end": 1979},
                "locally_built": False,
                "overview": "Heavy-duty commercial utility predating and overlapping early HiLux models, revered by Australian farmers.",
                "generations": [
                    {"series_code": "RK41/RK101", "generation_name": "Stout 2nd Gen", "years": {"start": 1964, "end": 1979}, "body_styles": ["Cab Chassis", "Single Cab Ute"], "summary": "1.9L 3R and 2.0L 5R engines, rugged solid chassis, 1.5-ton load carrying capability."}
                ]
            },
            {
                "model_slug": "lexcen",
                "name": "Lexcen",
                "vehicle_type": "Sedan / Wagon",
                "segment": "Large Car",
                "years_sold_au": {"start": 1989, "end": 1997},
                "locally_built": True,
                "overview": "Holden Commodore rebadged as a Toyota under the Button Plan joint venture (UAAI), built at Holden's Elizabeth plant.",
                "generations": [
                    {"series_code": "VN", "generation_name": "Lexcen VN", "years": {"start": 1989, "end": 1991}, "body_styles": ["Sedan", "Wagon"], "summary": "3.8L Buick V6, unique Toyota grille and badging; CSi, GLX, Newport."},
                    {"series_code": "VP", "generation_name": "Lexcen VP", "years": {"start": 1991, "end": 1993}, "body_styles": ["Sedan", "Wagon"], "summary": "IRS rear suspension available, CSi and Newport grades."},
                    {"series_code": "VR", "generation_name": "Lexcen VR", "years": {"start": 1993, "end": 1995}, "body_styles": ["Sedan", "Wagon"], "summary": "Driver airbag introduced, CSi, GLX, and Newport trims."},
                    {"series_code": "VS", "generation_name": "Lexcen VS", "years": {"start": 1995, "end": 1997}, "body_styles": ["Sedan", "Wagon"], "summary": "3.8L ECOTEC V6 engine 147kW, final model before UAAI venture dissolved."}
                ]
            },
            {
                "model_slug": "tarago",
                "name": "Tarago",
                "vehicle_type": "People Mover",
                "segment": "Van / People Mover",
                "years_sold_au": {"start": 1983, "end": 2019},
                "locally_built": False,
                "overview": "Australia's definitive family people mover for over three decades across four generations.",
                "generations": [
                    {"series_code": "YR22/CR21", "generation_name": "Tarago 1st Gen", "years": {"start": 1983, "end": 1990}, "body_styles": ["Van / People Mover"], "summary": "Cab-over design, 2.0L 3Y and 2.2L 4Y engines, 4WD versions available; DX and GL."},
                    {"series_code": "TCR10/11", "generation_name": "Tarago 2nd Gen ('Egg')", "years": {"start": 1990, "end": 2000}, "body_styles": ["People Mover"], "summary": "Futuristic mid-engine layout, 2.4L 2TZ-FE, GLi, GLX, and luxury Ultima."},
                    {"series_code": "ACR30/CLR30", "generation_name": "Tarago 3rd Gen", "years": {"start": 2000, "end": 2006}, "body_styles": ["People Mover"], "summary": "Front-engine FWD platform, 2.4L 2AZ-FE VVTi, sliding dual doors."},
                    {"series_code": "ACR50/GSR50", "generation_name": "Tarago 4th Gen", "years": {"start": 2006, "end": 2019}, "body_styles": ["People Mover"], "summary": "2.4L 4-cyl and 3.5L 2GR-FE V6 202kW; succeeded by Granvia in 2019."}
                ]
            },
            {
                "model_slug": "hiace",
                "name": "HiAce",
                "vehicle_type": "Van / Commuter Bus",
                "segment": "Commercial Van",
                "years_sold_au": {"start": 1971, "end": "Present"},
                "locally_built": False,
                "overview": "The ubiquitous Australian tradie, delivery, and camper van, legendary for million-kilometre reliability.",
                "generations": [
                    {"series_code": "H10", "generation_name": "HiAce 1st Gen", "years": {"start": 1971, "end": 1977}, "body_styles": ["Van", "Commuter"], "summary": "1.3L and 1.6L engines, cab-over commercial layout."},
                    {"series_code": "H20-H40", "generation_name": "HiAce 2nd Gen", "years": {"start": 1977, "end": 1982}, "body_styles": ["Van", "Commuter"], "summary": "1.6L 12R and 2.0L 18R petrol, first 2.2L L-series diesel models."},
                    {"series_code": "H50", "generation_name": "HiAce 3rd Gen", "years": {"start": 1982, "end": 1989}, "body_styles": ["Van", "Commuter"], "summary": "2.0L 3Y, 2.4L 2L diesel, wide-body and high-roof commuter bus variants."},
                    {"series_code": "H100", "generation_name": "HiAce 4th Gen", "years": {"start": 1989, "end": 2004}, "body_styles": ["Van", "Commuter"], "summary": "2.4L 2RZ-E, 2.8L 3L, and 3.0L 5L diesel; SBV semi-bonnet version 1995-2003."},
                    {"series_code": "H200", "generation_name": "HiAce 5th Gen", "years": {"start": 2004, "end": 2019}, "body_styles": ["LWB Van", "SLWB Van", "Commuter"], "summary": "3.0L 1KD-FTV turbo-diesel and 2.7L 2TR-FE petrol; dominant delivery vehicle."},
                    {"series_code": "H300", "generation_name": "HiAce 6th Gen", "years": {"start": 2019, "end": "Present"}, "body_styles": ["LWB Van", "SLWB Van", "Commuter"], "summary": "Semi-bonnet configuration for 5-star ANCAP safety, 2.8L 1GD-FTV turbo-diesel."}
                ]
            },
            {
                "model_slug": "86",
                "name": "86 / GR86",
                "vehicle_type": "Coupe",
                "segment": "Sports Car",
                "years_sold_au": {"start": 2012, "end": "Present"},
                "locally_built": False,
                "overview": "Lightweight, rear-wheel-drive sports coupe developed in partnership with Subaru, spiritual successor to the AE86 Sprinter.",
                "generations": [
                    {"series_code": "ZN6", "generation_name": "86 1st Gen", "years": {"start": 2012, "end": 2021}, "body_styles": ["Coupe"], "summary": "2.0L FA20 boxer engine 147kW/152kW with D-4S injection, 6-speed manual/auto; GT and GTS."},
                    {"series_code": "ZN8", "generation_name": "GR86 2nd Gen", "years": {"start": 2022, "end": "Present"}, "body_styles": ["Coupe"], "summary": "Gazoo Racing tuned 2.4L FA24 boxer 174kW/250Nm, stiffer chassis; GT and GTS."}
                ]
            }
        ]
    },
    {
        "make_slug": "mazda",
        "name": "Mazda",
        "country_of_origin": "Japan",
        "years_active_au": {"start": 1959, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "Renowned for innovative engineering, rotary-powered motorsport legends, and stylish consumer favourites. Mazda has consistently stood as Australia's second best-selling automotive marque for over two decades.",
        "australian_history": """Mazda vehicles first reached Australian shores in 1959 through independent distributors, with the tiny R360 rear-engine coupe and light commercial utility models. In 1966, the Mazda 1000/1200 Familia arrived, establishing Mazda's reputation for mechanical sophistication.

The pivotal chapter in Mazda's Australian heritage began in 1969 with the rotary engine revolution. Following the R100 coupe, Mazda introduced the Capella Rotary (RX-2) in 1970, the RX-3 in 1971, and the RX-4 in 1973. Australian motorsport legend Allan Moffat forged the RX-3 into an iconic touring car weapon, famously challenging the V8 Holden Toranas and Ford Falcons at Mount Panorama, Bathurst. The rotary legend culminated with three generations of the RX-7 sports car (1979-2002); Moffat won the Australian Touring Car Championship in 1983 in an RX-7, and Allan Horsley's Mazda Motorsport skunkworks built the world-exclusive, twin-turbo RX-7 SP in Melbourne to win the Eastern Creek and Bathurst 12 Hour endurance races in 1995.

In the mainstream market, Mazda forged a deep alliance with Ford Australia throughout the 1980s and 1990s. The front-wheel-drive Mazda 323 (BD/BF) and 626 (GC/GD) formed the engineering foundation for the locally built Ford Laser, Meteor, and Telstar, which dominated Australian sales charts.

In 1989, Mazda introduced the MX-5 (NA), a lightweight rear-wheel-drive roadster that single-handedly revitalized the open-top sports car segment in Australia and worldwide. In 1992, Mazda launched its luxury Eunos sub-brand in Australia, showcasing advanced engineering like the world's first Miller-cycle engine in the Eunos 800.

The modern era began in 2002 with Mazda's emotive 'Zoom-Zoom' brand renaissance. The Mazda6 (2002) and Mazda3 (2004) set new standards for design, build quality, and driving dynamics in their respective classes. In 2011 and 2012, the Mazda3 achieved the extraordinary feat of becoming Australia's #1 selling car outright, unseating the Holden Commodore. In 2012, the CX-5 introduced Skyactiv lightweight chassis and powertrain technology, becoming Australia's favourite private SUV for years. Today, Mazda Australia remains headquartered in Mulgrave, Victoria, backed by a nationwide dealer network.""",
        "models_catalog": [
            {
                "model_slug": "rx-7",
                "name": "RX-7",
                "vehicle_type": "Coupe",
                "segment": "Sports Car",
                "years_sold_au": {"start": 1979, "end": 2002},
                "locally_built": False,
                "overview": "Rotary-powered sports car icon with legendary Australian touring car and endurance racing heritage.",
                "generations": [
                    {"series_code": "SA22C/FB", "generation_name": "RX-7 Series 1-3", "years": {"start": 1979, "end": 1985}, "body_styles": ["Coupe"], "summary": "12A twin-rotor engine 77kW-85kW, 5-speed manual, Moffat ATCC winner 1983."},
                    {"series_code": "FC3S", "generation_name": "RX-7 Series 4-5", "years": {"start": 1986, "end": 1992}, "body_styles": ["Coupe", "Convertible"], "summary": "13B naturally aspirated and 13B-Turbo intercooled twin-scroll turbo (147kW-162kW)."},
                    {"series_code": "FD3S", "generation_name": "RX-7 Series 6-8", "years": {"start": 1992, "end": 2002}, "body_styles": ["Coupe"], "summary": "Sequential twin-turbo 13B-REW (176kW-206kW); 1995 Australian-only RX-7 SP homologation special."}
                ]
            },
            {
                "model_slug": "rx-8",
                "name": "RX-8",
                "vehicle_type": "Coupe",
                "segment": "Sports Car",
                "years_sold_au": {"start": 2003, "end": 2012},
                "locally_built": False,
                "overview": "4-door, 4-seat rotary sports coupe with rear suicide freestyle doors and the naturally aspirated RENESIS engine.",
                "generations": [
                    {"series_code": "SE3P", "generation_name": "RX-8 Series 1 & 2", "years": {"start": 2003, "end": 2012}, "body_styles": ["Coupe (Freestyle doors)"], "summary": "RENESIS 13B-MSP naturally aspirated rotary revving to 9000rpm (170kW-177kW); Base, Luxury, and GT."}
                ]
            },
            {
                "model_slug": "121",
                "name": "121",
                "vehicle_type": "Sedan / Hatchback",
                "segment": "Light Car",
                "years_sold_au": {"start": 1987, "end": 2002},
                "locally_built": False,
                "overview": "Quirky, beloved city car, famous in Australia for the DB 'Bubble' sedan and canvas 'Fun-top' roof.",
                "generations": [
                    {"series_code": "DA", "generation_name": "121 1st Gen", "years": {"start": 1987, "end": 1990}, "body_styles": ["3-door Hatch", "5-door Hatch"], "summary": "1.3L B3 engine, boxy packaging, co-developed with Ford Festiva."},
                    {"series_code": "DB", "generation_name": "121 2nd Gen ('Bubble')", "years": {"start": 1990, "end": 1996}, "body_styles": ["4-door Sedan"], "summary": "1.3L and 1.5L engines, distinctive rounded jellybean styling and canvas sunroof."},
                    {"series_code": "DW", "generation_name": "121 Metro 3rd Gen", "years": {"start": 1996, "end": 2002}, "body_styles": ["5-door Hatch"], "summary": "Tall-boy hatchback packaging, 1.3L and 1.5L engines, succeeded by Mazda2."}
                ]
            },
            {
                "model_slug": "mazda2",
                "name": "Mazda2",
                "vehicle_type": "Hatchback / Sedan",
                "segment": "Light Car",
                "years_sold_au": {"start": 2002, "end": "Present"},
                "locally_built": False,
                "overview": "Fun-to-drive, stylish light car that has been an Australian small-car mainstay for over two decades.",
                "generations": [
                    {"series_code": "DY", "generation_name": "Mazda2 1st Gen", "years": {"start": 2002, "end": 2007}, "body_styles": ["5-door Hatch"], "summary": "1.5L ZY-VE engine 82kW, tall mini-MPV profile; Neo, Maxx, and Genki."},
                    {"series_code": "DE", "generation_name": "Mazda2 2nd Gen", "years": {"start": 2007, "end": 2014}, "body_styles": ["3-door Hatch", "5-door Hatch", "Sedan"], "summary": "Gram-strategy lightweight chassis (100kg lighter), 1.5L MZR engine, Wheels COTY 2007."},
                    {"series_code": "DJ", "generation_name": "Mazda2 3rd Gen", "years": {"start": 2014, "end": "Present"}, "body_styles": ["5-door Hatch", "Sedan"], "summary": "KODO design, Skyactiv-G 1.5L engine (79kW-82kW), G-Vectoring Control; Pure, Evolve, GT."}
                ]
            },
            {
                "model_slug": "323",
                "name": "323",
                "vehicle_type": "Hatchback / Sedan / Wagon",
                "segment": "Small Car",
                "years_sold_au": {"start": 1977, "end": 2003},
                "locally_built": False,
                "overview": "Long-running small car range that cemented Mazda in Australia; platform twin to the Australian Ford Laser.",
                "generations": [
                    {"series_code": "FA4", "generation_name": "323 1st Gen", "years": {"start": 1977, "end": 1980}, "body_styles": ["Hatchback", "Wagon"], "summary": "Rear-wheel drive, 1.3L and 1.4L engines, hatch with folding rear seat."},
                    {"series_code": "BD", "generation_name": "323 2nd Gen", "years": {"start": 1980, "end": 1985}, "body_styles": ["Hatchback", "Sedan"], "summary": "Switch to FWD, 1.3L and 1.5L engines; Australian Wheels COTY 1980."},
                    {"series_code": "BF", "generation_name": "323 3rd Gen", "years": {"start": 1985, "end": 1989}, "body_styles": ["Hatchback", "Sedan", "Wagon"], "summary": "1.6L B6 engine, introduced turbo AWD variants in Japan; SS and Deluxe trims."},
                    {"series_code": "BG", "generation_name": "323 Astina 4th Gen", "years": {"start": 1989, "end": 1994}, "body_styles": ["Hatchback", "Sedan"], "summary": "Pop-up headlights on Astina 5-door, 1.6L and 1.8L DOHC engines; huge Australian cult status."},
                    {"series_code": "BA", "generation_name": "323 Astina/Protege 5th Gen", "years": {"start": 1994, "end": 1998}, "body_styles": ["Hatchback", "Sedan"], "summary": "Hardtop doors, 1.8L BP and smooth 2.0L KF-DE V6 engine in Astina V6."},
                    {"series_code": "BJ", "generation_name": "323 Astina/Protege 6th Gen", "years": {"start": 1998, "end": 2003}, "body_styles": ["Hatchback", "Sedan"], "summary": "1.6L ZM-DE, 1.8L FP-DE, and 2.0L FS-DE in Astina SP20; final 323 before Mazda3."}
                ]
            },
            {
                "model_slug": "mazda3",
                "name": "Mazda3",
                "vehicle_type": "Hatchback / Sedan",
                "segment": "Small Car",
                "years_sold_au": {"start": 2004, "end": "Present"},
                "locally_built": False,
                "overview": "One of Australia's most successful cars in modern history, twice topping the national sales charts outright (2011, 2012).",
                "generations": [
                    {"series_code": "BK", "generation_name": "Mazda3 1st Gen", "years": {"start": 2004, "end": 2009}, "body_styles": ["Hatchback", "Sedan"], "summary": "2.0L LF-VE, 2.3L L3-VE (SP23), and 190kW 2.3L Turbo MPS; Neo, Maxx, Maxx Sport, SP23."},
                    {"series_code": "BL", "generation_name": "Mazda3 2nd Gen", "years": {"start": 2009, "end": 2013}, "body_styles": ["Hatchback", "Sedan"], "summary": "Smiling face styling, 2.0L, 2.5L SP25, 2.2L Diesel, 190kW MPS; Australia's #1 car 2011 & 2012."},
                    {"series_code": "BM", "generation_name": "Mazda3 3rd Gen", "years": {"start": 2014, "end": 2016}, "body_styles": ["Hatchback", "Sedan"], "summary": "KODO styling, full Skyactiv-G 2.0L and 2.5L engines; Neo, Maxx, Touring, SP25, SP25 Astina."},
                    {"series_code": "BN", "generation_name": "Mazda3 3rd Gen Facelift", "years": {"start": 2016, "end": 2019}, "body_styles": ["Hatchback", "Sedan"], "summary": "Standard G-Vectoring Control, electronic park brake, updated interior."},
                    {"series_code": "BP", "generation_name": "Mazda3 4th Gen", "years": {"start": 2019, "end": "Present"}, "body_styles": ["Hatchback", "Sedan"], "summary": "Near-luxury finish, 2.0L G20, 2.5L G25, and Skyactiv-X SPCCI 2.0L mild hybrid (X20)."}
                ]
            },
            {
                "model_slug": "626",
                "name": "626",
                "vehicle_type": "Sedan / Hatchback / Wagon",
                "segment": "Mid-size Car",
                "years_sold_au": {"start": 1979, "end": 2002},
                "locally_built": False,
                "overview": "Refined Japanese mid-size car that challenged European competitors and shared DNA with the Ford Telstar.",
                "generations": [
                    {"series_code": "CB", "generation_name": "626 1st Gen", "years": {"start": 1979, "end": 1982}, "body_styles": ["Sedan", "Coupe"], "summary": "Rear-wheel drive, 2.0L MA engine, comfortable ride, Wheels COTY runner-up."},
                    {"series_code": "GC", "generation_name": "626 2nd Gen", "years": {"start": 1983, "end": 1987}, "body_styles": ["Sedan", "Hatchback"], "summary": "Switch to FWD, 2.0L FE engine, electronic adjustable suspension (EVCS); Wheels COTY 1983."},
                    {"series_code": "GD", "generation_name": "626 3rd Gen", "years": {"start": 1987, "end": 1992}, "body_styles": ["Sedan", "Hatchback", "Wagon"], "summary": "2.2L F2 engine, optional 4WS (four-wheel steering) and turbo variants."},
                    {"series_code": "GE", "generation_name": "626 4th Gen", "years": {"start": 1992, "end": 1997}, "body_styles": ["Sedan", "Hatchback"], "summary": "Sleek aerodynamic curves, 2.0L FS and smooth 2.5L KL-DE V6; Cronos architecture."},
                    {"series_code": "GF", "generation_name": "626 5th Gen", "years": {"start": 1997, "end": 2002}, "body_styles": ["Sedan", "Hatchback", "Wagon"], "summary": "2.0L FS-DE engine, spacious practical cabin; succeeded by Mazda6 in 2002."}
                ]
            },
            {
                "model_slug": "mazda6",
                "name": "Mazda6",
                "vehicle_type": "Sedan / Hatchback / Wagon",
                "segment": "Mid-size Car",
                "years_sold_au": {"start": 2002, "end": "Present"},
                "locally_built": False,
                "overview": "Dynamic mid-size sports sedan and wagon that spearheaded Mazda's 'Zoom-Zoom' brand rebirth in Australia.",
                "generations": [
                    {"series_code": "GG/GY", "generation_name": "Mazda6 1st Gen", "years": {"start": 2002, "end": 2008}, "body_styles": ["Sedan", "Hatchback", "Wagon"], "summary": "2.3L MZR engine 122kW, double-wishbone front suspension; 190kW AWD MPS turbo in 2005."},
                    {"series_code": "GH", "generation_name": "Mazda6 2nd Gen", "years": {"start": 2008, "end": 2012}, "body_styles": ["Sedan", "Hatchback", "Wagon"], "summary": "2.5L L5-VE petrol and 2.2L MZR-CD turbodiesel; Classic, Luxury, Luxury Sports."},
                    {"series_code": "GJ/GL", "generation_name": "Mazda6 3rd Gen", "years": {"start": 2012, "end": "Present"}, "body_styles": ["Sedan", "Wagon"], "summary": "KODO styling, Skyactiv-G 2.5L, 2.2L twin-turbo diesel, and 170kW 2.5L Turbo (Atenza)."}
                ]
            },
            {
                "model_slug": "mx-5",
                "name": "MX-5",
                "vehicle_type": "Roadster Convertible",
                "segment": "Sports Car",
                "years_sold_au": {"start": 1989, "end": "Present"},
                "locally_built": False,
                "overview": "The world's and Australia's favourite two-seat roadster, embodying the 'Jinba Ittai' (horse and rider as one) ethos.",
                "generations": [
                    {"series_code": "NA", "generation_name": "MX-5 1st Gen", "years": {"start": 1989, "end": 1997}, "body_styles": ["Roadster Convertible"], "summary": "Pop-up lights, 1.6L B6-ZE (85kW) then 1.8L BP-ZE (96kW); Wheels COTY 1989."},
                    {"series_code": "NB", "generation_name": "MX-5 2nd Gen", "years": {"start": 1998, "end": 2005}, "body_styles": ["Roadster Convertible"], "summary": "Fixed headlights, 1.8L BP-Z3 with VVT (106kW); 2002 Australian-only MX-5 SP Turbo (150kW)."},
                    {"series_code": "NC", "generation_name": "MX-5 3rd Gen", "years": {"start": 2005, "end": 2015}, "body_styles": ["Soft-top", "Retractable Hardtop (PRHT)"], "summary": "2.0L MZR LF-VE engine 118kW, flared guards, power retractable hardtop; Wheels COTY 2005."},
                    {"series_code": "ND", "generation_name": "MX-5 4th Gen", "years": {"start": 2015, "end": "Present"}, "body_styles": ["Soft-top", "Retractable Fastback (RF)"], "summary": "Sub-1000kg weight, Skyactiv-G 1.5L and 2.0L (135kW); Wheels COTY 2015."}
                ]
            },
            {
                "model_slug": "cx-3",
                "name": "CX-3",
                "vehicle_type": "SUV",
                "segment": "Light SUV",
                "years_sold_au": {"start": 2015, "end": "Present"},
                "locally_built": False,
                "overview": "Perennial best-seller in the Australian light SUV category, based on the Mazda2 platform.",
                "generations": [
                    {"series_code": "DK", "generation_name": "CX-3 1st Gen", "years": {"start": 2015, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "2.0L Skyactiv-G petrol (110kW) and 1.5L/1.8L diesel; Neo, Maxx, sTouring, Akari."}
                ]
            },
            {
                "model_slug": "cx-30",
                "name": "CX-30",
                "vehicle_type": "SUV",
                "segment": "Small SUV",
                "years_sold_au": {"start": 2020, "end": "Present"},
                "locally_built": False,
                "overview": "Sleek coupe-crossover bridging the gap between the CX-3 and CX-5, built on the Mazda3 architecture.",
                "generations": [
                    {"series_code": "DM", "generation_name": "CX-30 1st Gen", "years": {"start": 2020, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "2.0L G20, 2.5L G25, and Skyactiv-X mild hybrid; Pure, Evolve, Touring, Astina."}
                ]
            },
            {
                "model_slug": "cx-5",
                "name": "CX-5",
                "vehicle_type": "SUV",
                "segment": "Medium SUV",
                "years_sold_au": {"start": 2012, "end": "Present"},
                "locally_built": False,
                "overview": "The vehicle that solidified Mazda's SUV supremacy in Australia, repeatedly holding the title of Australia's #1 private SUV.",
                "generations": [
                    {"series_code": "KE", "generation_name": "CX-5 1st Gen", "years": {"start": 2012, "end": 2017}, "body_styles": ["5-door SUV"], "summary": "Launched Skyactiv technology; 2.0L petrol, 2.5L petrol, 2.2L twin-turbo diesel; Maxx, Maxx Sport, Grand Touring, Akari."},
                    {"series_code": "KF", "generation_name": "CX-5 2nd Gen", "years": {"start": 2017, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "Sculpted KODO body, G-Vectoring Control; added 170kW 2.5L Turbo in 2018."}
                ]
            },
            {
                "model_slug": "cx-7",
                "name": "CX-7",
                "vehicle_type": "SUV",
                "segment": "Medium SUV",
                "years_sold_au": {"start": 2006, "end": 2012},
                "locally_built": False,
                "overview": "Sporty crossover powered originally by the Mazda3 MPS turbo engine, an early precursor to the modern medium SUV boom.",
                "generations": [
                    {"series_code": "ER", "generation_name": "CX-7 1st Gen", "years": {"start": 2006, "end": 2012}, "body_styles": ["5-door SUV"], "summary": "2.3L Turbo MZR 175kW AWD, later 2.5L naturally aspirated FWD and 2.2L diesel."}
                ]
            },
            {
                "model_slug": "cx-8",
                "name": "CX-8",
                "vehicle_type": "SUV",
                "segment": "Large SUV",
                "years_sold_au": {"start": 2018, "end": 2023},
                "locally_built": False,
                "overview": "Narrower 7-seat family SUV blending CX-5 packaging with three-row capability, highly popular in diesel AWD.",
                "generations": [
                    {"series_code": "KG", "generation_name": "CX-8 1st Gen", "years": {"start": 2018, "end": 2023}, "body_styles": ["5-door SUV"], "summary": "2.2L twin-turbo diesel and 2.5L petrol; Sport, Touring, GT, Asaki."}
                ]
            },
            {
                "model_slug": "cx-9",
                "name": "CX-9",
                "vehicle_type": "SUV",
                "segment": "Large SUV",
                "years_sold_au": {"start": 2007, "end": 2023},
                "locally_built": False,
                "overview": "Spacious full-size 7-seat family SUV that won Wheels Car of the Year in 2008 and 2017 across two generations.",
                "generations": [
                    {"series_code": "TB", "generation_name": "CX-9 1st Gen", "years": {"start": 2007, "end": 2016}, "body_styles": ["5-door SUV"], "summary": "3.7L MZI V6 engine 204kW, 6-speed auto, FWD and AWD; Wheels COTY 2008."},
                    {"series_code": "TC", "generation_name": "CX-9 2nd Gen", "years": {"start": 2016, "end": 2023}, "body_styles": ["5-door SUV"], "summary": "2.5L Skyactiv-G Turbo 170kW/420Nm, premium cabin; Wheels COTY 2017."}
                ]
            },
            {
                "model_slug": "cx-60",
                "name": "CX-60",
                "vehicle_type": "SUV",
                "segment": "Medium Luxury SUV",
                "years_sold_au": {"start": 2023, "end": "Present"},
                "locally_built": False,
                "overview": "Mazda's premium push with rear-drive longitudinal architecture, inline-6 turbo engines, and plug-in hybrid options.",
                "generations": [
                    {"series_code": "KH", "generation_name": "CX-60 1st Gen", "years": {"start": 2023, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "3.3L Turbo Inline-6 petrol (209kW), 3.3L Inline-6 diesel (187kW), and 2.5L PHEV (241kW)."}
                ]
            },
            {
                "model_slug": "bt-50",
                "name": "BT-50",
                "vehicle_type": "Ute / Cab Chassis",
                "segment": "Light Commercial",
                "years_sold_au": {"start": 2006, "end": "Present"},
                "locally_built": False,
                "overview": "Heavy-duty dual-cab and single-cab ute, originally co-developed with Ford Ranger and now sharing underpinnings with the Isuzu D-Max.",
                "generations": [
                    {"series_code": "UN", "generation_name": "BT-50 1st Gen", "years": {"start": 2006, "end": 2011}, "body_styles": ["Single Cab", "Freestyle Cab", "Dual Cab"], "summary": "2.5L WL-C (105kW) and 3.0L WE-C (115kW) common-rail turbo-diesel; Ford Ranger PJ/PK twin."},
                    {"series_code": "UP/UR", "generation_name": "BT-50 2nd Gen", "years": {"start": 2011, "end": 2020}, "body_styles": ["Single Cab", "Freestyle Cab", "Dual Cab"], "summary": "Ford Ranger PX platform, 3.2L 5-cylinder diesel (147kW/470Nm) and 2.2L 4-cylinder; XT, XTR, GT."},
                    {"series_code": "TF", "generation_name": "BT-50 3rd Gen", "years": {"start": 2020, "end": "Present"}, "body_styles": ["Single Cab", "Freestyle Cab", "Dual Cab"], "summary": "Isuzu D-Max platform, 3.0L 4JJ3-TCX diesel (140kW/450Nm) and 1.9L; XT, XTR, GT, SP, Thunder."}
                ]
            }
        ]
    },
    {
        "make_slug": "mitsubishi",
        "name": "Mitsubishi",
        "country_of_origin": "Japan",
        "years_active_au": {"start": 1980, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": True,
        "overview": "From manufacturing over 1.1 million cars at Tonsley Park, South Australia to dominating outback tracks with the Pajero and Triton, Mitsubishi is embedded in Australia's automotive fabric.",
        "australian_history": """Mitsubishi's connection with Australia began in the 1960s through Chrysler Australia, which sold the Colt 1000 and, in 1971, introduced the Galant. In 1977, Chrysler Australia launched the Chrysler Sigma (based on the Japanese Galant), assembled at Chrysler's Tonsley Park plant in Adelaide, South Australia. The Sigma became an instant national sensation, dominating the 4-cylinder market.

In 1980, Mitsubishi Motors Corporation acquired Chrysler Australia, establishing Mitsubishi Motors Australia Limited (MMAL). MMAL invested heavily in South Australia, operating vehicle assembly at Tonsley Park and an engine casting foundry at Lonsdale. In 1985, MMAL launched the groundbreaking TM Magna. Engineered specifically for Australian family motoring, MMAL took the Japanese Galant and widened the body by 66mm to create a spacious mid-to-large car perfectly suited to Australian wide-open spaces. Powered by the locally made 2.6L Astron II engine, the Magna won the 1985 Wheels Car of the Year.

In 1991, MMAL launched the second-generation TR Magna and luxury KR Verada, introducing a 3.0L V6. The Australian-developed Magna wagon and sedan were exported in huge numbers to the United States (as the Mitsubishi Diamante), Japan, and the UK, demonstrating world-class Australian manufacturing capability. In 1996, the third-generation TE Magna won Wheels Car of the Year again. In 2002, MMAL created the Magna Ralliart (180kW hand-built 3.5L V6) and the world-first Magna All-Wheel Drive (AWD) utilizing the QuadTec system. In 2005, the Magna was replaced by the 380 sedan (DB series) following a $600M plant overhaul. However, shifting consumer demand away from large local sedans led MMAL to close Tonsley Park on March 27, 2008.

Following the end of domestic manufacturing, Mitsubishi successfully pivoted to a 100% imported range focused on SUVs and utes. The Pajero established legendary 4WD status across four generations (1983-2021). The Triton ute became one of Australia's top three light commercial vehicles. In 2014, the Outlander PHEV pioneered affordable plug-in hybrid technology in Australia, remaining the nation's best-selling PHEV SUV.""",
        "models_catalog": [
            {
                "model_slug": "sigma",
                "name": "Sigma",
                "vehicle_type": "Sedan / Wagon",
                "segment": "Mid-size Car",
                "years_sold_au": {"start": 1977, "end": 1987},
                "locally_built": True,
                "overview": "The car that transformed Tonsley Park; originally sold under Chrysler, then Mitsubishi from 1980.",
                "generations": [
                    {"series_code": "GE/GH", "generation_name": "Chrysler Sigma 1st Gen", "years": {"start": 1977, "end": 1980}, "body_styles": ["Sedan", "Wagon"], "summary": "1.6L Saturn, 1.85L and 2.0L Astron engines; Galant-based Australian family favourite."},
                    {"series_code": "GJ/GK/GN", "generation_name": "Mitsubishi Sigma 2nd Gen", "years": {"start": 1980, "end": 1987}, "body_styles": ["Sedan", "Wagon"], "summary": "2.0L and 2.6L Astron engines, Peter Wherrett special edition, 5-speed manual; Tonsley Park built."}
                ]
            },
            {
                "model_slug": "magna",
                "name": "Magna",
                "vehicle_type": "Sedan / Wagon",
                "segment": "Large Car",
                "years_sold_au": {"start": 1985, "end": 2005},
                "locally_built": True,
                "overview": "Australia's widebody family car triumph, manufactured across three generations at Tonsley Park, South Australia.",
                "generations": [
                    {"series_code": "TM/TN/TP", "generation_name": "Magna 1st Gen", "years": {"start": 1985, "end": 1991}, "body_styles": ["Sedan", "Wagon"], "summary": "2.6L Astron II (carburetted and EFI), widebody Galant platform, Wheels COTY 1985; GLX, SE, Elite."},
                    {"series_code": "TR/TS", "generation_name": "Magna 2nd Gen", "years": {"start": 1991, "end": 1996}, "body_styles": ["Sedan", "Wagon"], "summary": "2.6L 4-cyl and 3.0L 6G72 V6; Executive, SE, Elite; exported globally as Diamante wagon."},
                    {"series_code": "TE-TW", "generation_name": "Magna 3rd Gen", "years": {"start": 1996, "end": 2005}, "body_styles": ["Sedan", "Wagon"], "summary": "3.0L and 3.5L 6G74 V6; Wheels COTY 1996; Magna Ralliart (180kW) and Magna AWD (QuadTec)."}
                ]
            },
            {
                "model_slug": "verada",
                "name": "Verada",
                "vehicle_type": "Sedan / Wagon",
                "segment": "Large Luxury Car",
                "years_sold_au": {"start": 1991, "end": 2005},
                "locally_built": True,
                "overview": "Tonsley Park-built luxury derivative of the Magna, featuring extended equipment, V6 power, and exported as the Diamante.",
                "generations": [
                    {"series_code": "KR/KS", "generation_name": "Verada 1st Gen", "years": {"start": 1991, "end": 1996}, "body_styles": ["Sedan", "Wagon"], "summary": "3.0L 6G72 V6, 4-speed automatic, electronic suspension, ABS, Ei and Xi grades."},
                    {"series_code": "KE-KW", "generation_name": "Verada 2nd Gen", "years": {"start": 1996, "end": 2005}, "body_styles": ["Sedan", "Wagon"], "summary": "3.5L 6G74 V6, leather trim, premium audio, AWD option (Verada AWD); Ei, Xi, GTV."}
                ]
            },
            {
                "model_slug": "380",
                "name": "380",
                "vehicle_type": "Sedan",
                "segment": "Large Car",
                "years_sold_au": {"start": 2005, "end": 2008},
                "locally_built": True,
                "overview": "The final car manufactured by Mitsubishi in Australia at Tonsley Park, praised for exceptional chassis dynamics and 3.8L V6 power.",
                "generations": [
                    {"series_code": "DB", "generation_name": "380 Series I-III", "years": {"start": 2005, "end": 2008}, "body_styles": ["Sedan"], "summary": "3.8L 6G75 V6 (175kW), 5-speed auto/manual; Base, SX, VRX, GT, LX; final car built 27 Mar 2008."}
                ]
            },
            {
                "model_slug": "colt",
                "name": "Colt",
                "vehicle_type": "Hatchback / Sedan",
                "segment": "Light / Small Car",
                "years_sold_au": {"start": 1982, "end": 2012},
                "locally_built": True,
                "overview": "Compact city car, built at Tonsley Park in the 1980s and re-introduced in the 2000s including the Colt Ralliart Turbo.",
                "generations": [
                    {"series_code": "RB-RE", "generation_name": "Colt (Local Build)", "years": {"start": 1982, "end": 1990}, "body_styles": ["5-door Hatch", "4-door Sedan"], "summary": "1.4L and 1.6L Saturn engines, Twin-Stick dual-range manual, assembled in Adelaide."},
                    {"series_code": "RG", "generation_name": "Colt (Imported)", "years": {"start": 2004, "end": 2012}, "body_styles": ["5-door Hatch", "Cabriolet"], "summary": "1.5L 4A91 petrol, CVT; Ralliart version with 1.5L 4G15 Turbo 113kW, 5-speed manual."}
                ]
            },
            {
                "model_slug": "mirage",
                "name": "Mirage",
                "vehicle_type": "Hatchback / Sedan",
                "segment": "Light Car",
                "years_sold_au": {"start": 1996, "end": 2021},
                "locally_built": False,
                "overview": "Affordable 3-door hatch in the 1990s and later a fuel-efficient 5-door micro car.",
                "generations": [
                    {"series_code": "CE", "generation_name": "Mirage 1st Gen (AU)", "years": {"start": 1996, "end": 2004}, "body_styles": ["3-door Hatch"], "summary": "1.5L 4G15 64kW, sporty budget 3-door hatchback, popular first car in Australia."},
                    {"series_code": "LA/LB", "generation_name": "Mirage 2nd Gen (AU)", "years": {"start": 2013, "end": 2021}, "body_styles": ["5-door Hatch", "4-door Sedan"], "summary": "1.2L 3-cylinder 3A92 engine, 4.6L/100km fuel economy; ES, LS, GT."}
                ]
            },
            {
                "model_slug": "lancer",
                "name": "Lancer",
                "vehicle_type": "Sedan / Hatchback / Coupe / Wagon",
                "segment": "Small Car",
                "years_sold_au": {"start": 1977, "end": 2019},
                "locally_built": False,
                "overview": "A cornerstone of Australia's small car market for four decades, renowned for bulletproof reliability and the legendary Evolution rally series.",
                "generations": [
                    {"series_code": "A70/LC", "generation_name": "Lancer 1st/2nd Gen", "years": {"start": 1977, "end": 1983}, "body_styles": ["2-door Sedan", "4-door Sedan", "Hatchback"], "summary": "1.4L and 1.6L Saturn engines, rear-wheel drive, Southern Cross Rally heritage."},
                    {"series_code": "CA/CB/CC", "generation_name": "Lancer 3rd/4th Gen", "years": {"start": 1989, "end": 1996}, "body_styles": ["Hatchback", "Sedan", "Coupe", "Wagon"], "summary": "1.5L 4G15, 1.6L, 1.8L DOHC GSR Turbo AWD 141kW; GL, GLXi, Executive."},
                    {"series_code": "CE", "generation_name": "Lancer 5th Gen", "years": {"start": 1996, "end": 2003}, "body_styles": ["Coupe", "Sedan", "Wagon"], "summary": "1.5L, 1.8L 4G93; GLi, GLXi, MR; foundation for Evolution IV-VI Australian rally dominance."},
                    {"series_code": "CG/CH", "generation_name": "Lancer 6th Gen", "years": {"start": 2002, "end": 2007}, "body_styles": ["Sedan", "Wagon"], "summary": "2.0L 4G94 and 2.4L 4G69 MIVEC in VR-X; official Australian imports of Evolution VII-IX."},
                    {"series_code": "CJ/CF", "generation_name": "Lancer 7th Gen", "years": {"start": 2007, "end": 2019}, "body_styles": ["Sedan", "Sportback Hatch"], "summary": "Shark-nose styling, 2.0L 4B11, 2.4L 4B12 (VRX), 177kW Ralliart Turbo AWD, and 217kW Evolution X."}
                ]
            },
            {
                "model_slug": "pajero",
                "name": "Pajero",
                "vehicle_type": "4WD Wagon",
                "segment": "Large 4WD SUV",
                "years_sold_au": {"start": 1983, "end": 2021},
                "locally_built": False,
                "overview": "Multi-time Dakar Rally champion that defined the multi-purpose family 4WD wagon in Australia for nearly four decades.",
                "generations": [
                    {"series_code": "NA-NG", "generation_name": "Pajero 1st Gen", "years": {"start": 1983, "end": 1991}, "body_styles": ["SWB 3-door", "LWB 5-door"], "summary": "2.6L 4G54 petrol, 2.5L 4D56 turbo-diesel, 3.0L V6; rear leaf springs, dual-range 4WD."},
                    {"series_code": "NH-NL", "generation_name": "Pajero 2nd Gen", "years": {"start": 1991, "end": 2000}, "body_styles": ["SWB 3-door", "LWB 5-door"], "summary": "Super Select 4WD pioneer, 3.0L/3.5L V6, 2.8L turbo-diesel; GL, GLS, Exceed."},
                    {"series_code": "NM-NP", "generation_name": "Pajero 3rd Gen", "years": {"start": 2000, "end": 2006}, "body_styles": ["SWB 3-door", "LWB 5-door"], "summary": "Monocoque body with integrated chassis, IRS, 3.2L 4M41 Di-D diesel and 3.5L/3.8L V6."},
                    {"series_code": "NS-NX", "generation_name": "Pajero 4th Gen", "years": {"start": 2006, "end": 2021}, "body_styles": ["SWB 3-door", "LWB 5-door"], "summary": "3.2L common-rail Di-D diesel (147kW/441Nm), Super Select II; concluded with 2021 Final Edition."}
                ]
            },
            {
                "model_slug": "pajero-sport",
                "name": "Pajero Sport",
                "vehicle_type": "SUV",
                "segment": "Large 4WD SUV",
                "years_sold_au": {"start": 2015, "end": "Present"},
                "locally_built": False,
                "overview": "Triton-based 7-seat 4WD wagon with coil-spring rear suspension and Super Select II 4WD.",
                "generations": [
                    {"series_code": "QE/QF", "generation_name": "Pajero Sport 1st Gen (AU)", "years": {"start": 2015, "end": "Present"}, "body_styles": ["5-door Wagon"], "summary": "2.4L 4N15 MIVEC turbo-diesel 133kW/430Nm, 8-speed automatic, 3100kg towing; GLX, GLS, Exceed, GSR."}
                ]
            },
            {
                "model_slug": "challenger",
                "name": "Challenger",
                "vehicle_type": "SUV",
                "segment": "Large 4WD SUV",
                "years_sold_au": {"start": 1998, "end": 2015},
                "locally_built": False,
                "overview": "Predecessor to the Pajero Sport, offering Triton-based rugged 4WD wagon capability.",
                "generations": [
                    {"series_code": "PA", "generation_name": "Challenger 1st Gen", "years": {"start": 1998, "end": 2006}, "body_styles": ["5-door Wagon"], "summary": "3.0L 6G72 V6 petrol engine, dual-range 4WD, ladder frame chassis."},
                    {"series_code": "PB/PC", "generation_name": "Challenger 2nd Gen", "years": {"start": 2009, "end": 2015}, "body_styles": ["5-door Wagon"], "summary": "2.5L 4D56 High-Power turbo-diesel 131kW/400Nm, Super Select 4WD, 5 or 7 seats."}
                ]
            },
            {
                "model_slug": "triton",
                "name": "Triton",
                "vehicle_type": "Ute / Cab Chassis",
                "segment": "Light Commercial",
                "years_sold_au": {"start": 1979, "end": "Present"},
                "locally_built": False,
                "overview": "From the original L200 to modern dual-cabs, Triton has been an Australian tradie and 4WD touring hero.",
                "generations": [
                    {"series_code": "ME-MK", "generation_name": "Triton 1st/2nd Gen (AU)", "years": {"start": 1986, "end": 2006}, "body_styles": ["Single Cab", "Club Cab", "Double Cab"], "summary": "2.6L 4G54 petrol, 2.8L 4M40 diesel, 3.0L V6; GL, GLX, GLS."},
                    {"series_code": "ML/MN", "generation_name": "Triton 4th Gen", "years": {"start": 2006, "end": 2015}, "body_styles": ["Single Cab", "Club Cab", "Double Cab"], "summary": "Curved J-line cabin styling, 3.2L 4M41 and 2.5L 4D56 diesel, 3.5L V6; GLX-R."},
                    {"series_code": "MQ/MR", "generation_name": "Triton 5th Gen", "years": {"start": 2015, "end": 2023}, "body_styles": ["Single Cab", "Club Cab", "Double Cab"], "summary": "2.4L 4N15 MIVEC turbo-diesel 133kW/430Nm, Dynamic Shield styling, Super Select II; GLS, GSR."},
                    {"series_code": "MV", "generation_name": "Triton 6th Gen", "years": {"start": 2024, "end": "Present"}, "body_styles": ["Double Cab", "Club Cab"], "summary": "All-new wider ladder chassis, 2.4L 4N16 bi-turbo diesel 150kW/470Nm, 3500kg towing."}
                ]
            },
            {
                "model_slug": "asx",
                "name": "ASX",
                "vehicle_type": "SUV",
                "segment": "Small SUV",
                "years_sold_au": {"start": 2010, "end": "Present"},
                "locally_built": False,
                "overview": "One of Australia's longest-running and highest-selling compact SUVs, celebrated for honest value and space.",
                "generations": [
                    {"series_code": "XA/XB/XC", "generation_name": "ASX 1st Gen", "years": {"start": 2010, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "2.0L 4B11 and 2.4L 4B12 petrol, 1.8L/2.2L turbo-diesel; ES, MR, LS, GSR, Exceed."}
                ]
            },
            {
                "model_slug": "outlander",
                "name": "Outlander",
                "vehicle_type": "SUV",
                "segment": "Medium SUV",
                "years_sold_au": {"start": 2003, "end": "Present"},
                "locally_built": False,
                "overview": "Versatile 5 and 7-seat family SUV that pioneered mass-market plug-in hybrid motoring in Australia.",
                "generations": [
                    {"series_code": "ZE/ZF", "generation_name": "Outlander 1st Gen", "years": {"start": 2003, "end": 2006}, "body_styles": ["5-door SUV"], "summary": "2.4L 4G69 MIVEC engine, AWD, sporty crossover styling; LS and XLS."},
                    {"series_code": "ZG/ZH", "generation_name": "Outlander 2nd Gen", "years": {"start": 2006, "end": 2012}, "body_styles": ["5-door SUV"], "summary": "2.4L 4-cyl and 3.0L 6B31 V6, split fold-down tailgate, available 7 seats."},
                    {"series_code": "ZJ/ZK/ZL", "generation_name": "Outlander 3rd Gen", "years": {"start": 2012, "end": 2021}, "body_styles": ["5-door SUV"], "summary": "2.0L/2.4L petrol, 2.2L diesel, and revolutionary 2014 Outlander PHEV (first mainstream PHEV SUV in AU)."},
                    {"series_code": "ZM", "generation_name": "Outlander 4th Gen", "years": {"start": 2021, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "CMF-C/D platform, 2.5L petrol and 2.4L PHEV with 20kWh battery and twin electric motors (S-AWC)."}
                ]
            },
            {
                "model_slug": "eclipse-cross",
                "name": "Eclipse Cross",
                "vehicle_type": "SUV",
                "segment": "Small / Medium SUV",
                "years_sold_au": {"start": 2017, "end": "Present"},
                "locally_built": False,
                "overview": "Coupe-SUV styling with turbo and plug-in hybrid options, slotting between ASX and Outlander.",
                "generations": [
                    {"series_code": "YA", "generation_name": "Eclipse Cross 1st Gen", "years": {"start": 2017, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "1.5L 4B40 Turbo petrol 110kW and 2.4L PHEV twin-motor AWD; ES, LS, Aspire, Exceed."}
                ]
            }
        ]
    },
    {
        "make_slug": "nissan",
        "name": "Nissan",
        "country_of_origin": "Japan",
        "years_active_au": {"start": 1934, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": True,
        "overview": "From the Datsun 1600 and local manufacturing at Clayton, Victoria, to the legendary 'Godzilla' Skyline GT-R and indestructible Patrol, Nissan is central to Australian motoring history.",
        "australian_history": """Nissan's roots in Australia extend back to 1934 when early Datsuns were imported in modest numbers. A major public breakthrough came in 1958 when two Datsun 210 sedans finished the punishing Mobilgas Round Australia Rally, proving Japanese engineering resilience to a skeptical public.

In 1966, Nissan Motor Company (Australia) was formed. To satisfy local content regulations, Nissan contracted Motor Producers Limited (the former Volkswagen assembly plant) at Clayton, Victoria and Pressed Metal Corporation in Sydney to assemble Datsun passenger cars. In 1968, the Datsun 1600 (510) launched, immediately becoming a sensation. With its overhead cam engine and independent rear suspension, it dominated Australian rallying and club motorsport. Subsequent Datsuns like the 1200, 180B, 200B, and the iconic 240Z sports car (1970) made Datsun a household name.

In 1976, Nissan acquired the Clayton plant outright, creating Nissan Motor Manufacturing Australia (NMMA). Nissan phased out the Datsun nameplate in favour of Nissan between 1981 and 1984. Clayton produced the Bluebird, Pintara, and the Australian-engineered R31 Skyline sedan and wagon, powered by an imported 3.0L RB30E inline-6. Under the Federal Government's Button Plan, Nissan built the Pintara for Ford to sell as the Ford Corsair, while Ford supplied Falcon utilities to Nissan.

In 1990-1992, Fred Gibson's Nissan Motorsport team unleashed the R32 Skyline GT-R in the Australian Touring Car Championship. Dubbed 'Godzilla' by Wheels magazine, the twin-turbo, all-wheel-drive GT-R smashed the V8 competition, winning back-to-back Bathurst 1000s in 1991 and 1992 with Jim Richards and Mark Skaife. This dominance precipitated the demise of Group A and the creation of V8 Supercars.

Mounting financial losses under reduced tariff protections led Nissan to cease vehicle assembly at Clayton in 1992, though Nissan retained the Clayton Casting Plant to manufacture aluminum transmission components. As a full importer, Nissan achieved tremendous success with the Patrol (GQ, GU, Y62), Navara ute, X-Trail SUV, and Z sports cars. Nissan was also an early EV pioneer, launching the Leaf in Australia in 2012. In 2019, Nissan partnered with Premcar in Melbourne to develop the locally engineered 'Warrior' range of Navara and Patrol.""",
        "models_catalog": [
            {
                "model_slug": "patrol",
                "name": "Patrol",
                "vehicle_type": "4WD Wagon / Cab Chassis",
                "segment": "Upper Large 4WD",
                "years_sold_au": {"start": 1962, "end": "Present"},
                "locally_built": False,
                "overview": "The LandCruiser's fiercest rival, an indestructible heavy-duty 4WD that made history as the first vehicle to cross the Simpson Desert in 1962.",
                "generations": [
                    {"series_code": "G60", "generation_name": "Patrol G60", "years": {"start": 1962, "end": 1980}, "body_styles": ["SWB Soft/Hardtop", "LWB Wagon", "Cab Chassis"], "summary": "4.0L P40 inline-6 petrol, solid leaf axles, first vehicle to cross the Simpson Desert (1962)."},
                    {"series_code": "MQ/MK", "generation_name": "Patrol MQ / MK", "years": {"start": 1980, "end": 1987}, "body_styles": ["Hardtop", "Wagon", "Cab Chassis"], "summary": "SD33 3.3L diesel and SD33T turbo-diesel, L28 2.8L and P40 4.0L petrol; 4-speed/5-speed manual."},
                    {"series_code": "GQ/Y60", "generation_name": "Patrol GQ", "years": {"start": 1987, "end": 1997}, "body_styles": ["Wagon", "Cab Chassis"], "summary": "All-coil suspension revolution, legendary TD42 4.2L diesel and TB42 4.2L petrol; also sold as Ford Maverick."},
                    {"series_code": "GU/Y61", "generation_name": "Patrol GU", "years": {"start": 1997, "end": 2016}, "body_styles": ["Wagon", "Cab Chassis"], "summary": "TD42T/Ti 4.2L turbo-diesel, ZD30 3.0L turbo-diesel, and TB48DE 4.8L petrol (185kW); DX, ST, Ti."},
                    {"series_code": "Y62", "generation_name": "Patrol Y62", "years": {"start": 2013, "end": "Present"}, "body_styles": ["Wagon"], "summary": "5.6L VK56VD V8 petrol 298kW/560Nm, 7-speed auto, Hydraulic Body Motion Control; Ti, Ti-L, Warrior."}
                ]
            },
            {
                "model_slug": "skyline",
                "name": "Skyline",
                "vehicle_type": "Sedan / Wagon / Coupe",
                "segment": "Mid-size / Large Sports",
                "years_sold_au": {"start": 1973, "end": 2002},
                "locally_built": True,
                "overview": "Australian-assembled family hero in R31 guise, and Bathurst-dominating 'Godzilla' GT-R icon.",
                "generations": [
                    {"series_code": "C110/C210", "generation_name": "Datsun 240K / Skyline", "years": {"start": 1973, "end": 1981}, "body_styles": ["Sedan", "Coupe"], "summary": "L24 2.4L OHC inline-6, GL and GT trims, distinctive round taillights."},
                    {"series_code": "R30", "generation_name": "Skyline R30", "years": {"start": 1981, "end": 1985}, "body_styles": ["Sedan", "Hatchback"], "summary": "L24E 2.4L EFI inline-6, imported sedan and five-door hatchback."},
                    {"series_code": "R31", "generation_name": "Skyline R31 (Clayton Build)", "years": {"start": 1986, "end": 1991}, "body_styles": ["Sedan", "Station Wagon"], "summary": "Locally built at Clayton; RB30E 3.0L inline-6 (114kW); Silhouette, Ti, and Gibson GTS1/GTS2 (140kW)."},
                    {"series_code": "R32", "generation_name": "Skyline R32 GT-R ('Godzilla')", "years": {"start": 1989, "end": 1994}, "body_styles": ["Coupe"], "summary": "100 official Australian-delivered GT-Rs (1991); RB26DETT twin-turbo AWD, Bathurst 1000 winner 1991 & 1992."},
                    {"series_code": "R33/R34", "generation_name": "Skyline R33 / R34", "years": {"start": 1993, "end": 2002}, "body_styles": ["Coupe", "Sedan"], "summary": "RB25DET and RB26DETT GT-R, cult enthusiast imports and special deliveries."}
                ]
            },
            {
                "model_slug": "navara",
                "name": "Navara",
                "vehicle_type": "Ute / Cab Chassis",
                "segment": "Light Commercial",
                "years_sold_au": {"start": 1986, "end": "Present"},
                "locally_built": False,
                "overview": "From the D21 through the D40 and NP300, Navara has been a central player in Australia's competitive dual-cab ute market.",
                "generations": [
                    {"series_code": "D21", "generation_name": "Navara D21", "years": {"start": 1986, "end": 1997}, "body_styles": ["Single Cab", "King Cab", "Dual Cab"], "summary": "2.4L Z24/KA24 petrol, 2.7L TD27 diesel, 3.0L VG30E V6; DX and ST grades."},
                    {"series_code": "D22", "generation_name": "Navara D22", "years": {"start": 1997, "end": 2015}, "body_styles": ["Single Cab", "King Cab", "Dual Cab"], "summary": "3.0L ZD30 and 2.5L YD25 common-rail turbo-diesel, 3.3L VG33E V6; rugged budget favourite."},
                    {"series_code": "D40", "generation_name": "Navara D40", "years": {"start": 2005, "end": 2015}, "body_styles": ["King Cab", "Dual Cab"], "summary": "Spanish/Thai built, 2.5L YD25 (126-140kW), 4.0L V6 petrol, and 170kW 3.0L V9X V6 turbo-diesel; ST-X."},
                    {"series_code": "D23/NP300", "generation_name": "Navara D23 / NP300", "years": {"start": 2015, "end": "Present"}, "body_styles": ["Single Cab", "King Cab", "Dual Cab"], "summary": "Coil-spring multi-link rear suspension, 2.3L twin-turbo diesel YS23DDTT; ST, ST-X, PRO-4X, and Premcar Warrior."}
                ]
            },
            {
                "model_slug": "x-trail",
                "name": "X-Trail",
                "vehicle_type": "SUV",
                "segment": "Medium SUV",
                "years_sold_au": {"start": 2001, "end": "Present"},
                "locally_built": False,
                "overview": "Versatile and family-friendly compact SUV, consistently one of Australia's best-selling medium SUVs.",
                "generations": [
                    {"series_code": "T30", "generation_name": "X-Trail 1st Gen", "years": {"start": 2001, "end": 2007}, "body_styles": ["5-door SUV"], "summary": "2.5L QR25DE engine 132kW, All-Mode 4x4, washable cargo floor, central instrument cluster; ST and Ti."},
                    {"series_code": "T31", "generation_name": "X-Trail 2nd Gen", "years": {"start": 2007, "end": 2014}, "body_styles": ["5-door SUV"], "summary": "Boxy styling, 2.5L petrol and 2.0L M9R turbo-diesel, drawer storage system; ST, ST-L, Ti, TL."},
                    {"series_code": "T32", "generation_name": "X-Trail 3rd Gen", "years": {"start": 2014, "end": 2022}, "body_styles": ["5-door SUV"], "summary": "Aerodynamic curves, available 7 seats, 2.0L/2.5L petrol and 1.6L/2.0L diesel; ST, ST-L, Ti."},
                    {"series_code": "T33", "generation_name": "X-Trail 4th Gen", "years": {"start": 2022, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "CMF-C platform, 2.5L PR25DD petrol and e-POWER series hybrid with e-4ORCE electric AWD."}
                ]
            },
            {
                "model_slug": "pulsar",
                "name": "Pulsar",
                "vehicle_type": "Hatchback / Sedan",
                "segment": "Small Car",
                "years_sold_au": {"start": 1980, "end": "Present"},
                "locally_built": True,
                "overview": "Mass-market small car hero built at Clayton through the 1980s and early 1990s, famous for the SSS turbo and SSS hot hatch badges.",
                "generations": [
                    {"series_code": "N10", "generation_name": "Pulsar / Datsun 310", "years": {"start": 1980, "end": 1982}, "body_styles": ["3-door Hatch", "5-door Hatch"], "summary": "1.3L and 1.4L A-series engines, FWD transition."},
                    {"series_code": "N12", "generation_name": "Pulsar N12 (Clayton Build)", "years": {"start": 1982, "end": 1987}, "body_styles": ["Hatchback", "Sedan"], "summary": "Clayton assembly; E13 and E15 engines; Holden shared under Astra badge; ET Turbo with E15ET 77kW."},
                    {"series_code": "N13", "generation_name": "Pulsar N13 (Clayton Build)", "years": {"start": 1987, "end": 1991}, "body_styles": ["Hatchback", "Sedan"], "summary": "1.6L and 1.8L Family II engines (from Holden engine plant); Vector and SSS models."},
                    {"series_code": "N14", "generation_name": "Pulsar N14", "years": {"start": 1991, "end": 1995}, "body_styles": ["Hatchback", "Sedan"], "summary": "Imported from Japan; GA16DE 1.6L and legendary SR20DE 2.0L 105kW in the Pulsar SSS."},
                    {"series_code": "N15", "generation_name": "Pulsar N15", "years": {"start": 1995, "end": 2000}, "body_styles": ["Hatchback", "Sedan"], "summary": "1.6L GA16DE and 2.0L SR20DE in SSS; LX, Q, and SSS trims; huge Australian sales volume."},
                    {"series_code": "N16", "generation_name": "Pulsar N16", "years": {"start": 2000, "end": 2006}, "body_styles": ["Hatchback", "Sedan"], "summary": "1.6L and 1.8L QG18DE engines; ST, Q, and Ti grades."},
                    {"series_code": "B17/C12", "generation_name": "Pulsar B17 / C12", "years": {"start": 2013, "end": "Present"}, "body_styles": ["Sedan", "Hatchback"], "summary": "1.8L MRA8DE petrol and 1.6L DIG-Turbo MR16DDT 140kW in revived SSS hatch."}
                ]
            },
            {
                "model_slug": "z-car",
                "name": "Z-Car",
                "vehicle_type": "Coupe / Convertible",
                "segment": "Sports Car",
                "years_sold_au": {"start": 1970, "end": "Present"},
                "locally_built": False,
                "overview": "From the Datsun 240Z in 1970 to the modern twin-turbo Nissan Z, the Fairlady Z bloodline is an Australian sports car institution.",
                "generations": [
                    {"series_code": "S30", "generation_name": "240Z / 260Z", "years": {"start": 1970, "end": 1978}, "body_styles": ["Coupe", "2+2 Coupe"], "summary": "L24 2.4L and L26/L28 2.6L inline-6 engines; hit of the 1970s Australian sports car market."},
                    {"series_code": "S130", "generation_name": "280ZX", "years": {"start": 1978, "end": 1983}, "body_styles": ["Coupe", "T-Bar Roof 2+2"], "summary": "2.8L L28E EFI inline-6, luxury grand tourer features, power steering, T-bar roof."},
                    {"series_code": "Z31", "generation_name": "300ZX Z31", "years": {"start": 1984, "end": 1989}, "body_styles": ["Coupe", "T-Bar 2+2"], "summary": "3.0L VG30E and VG30ET Turbo V6 engines, pop-up headlights, digital instrumentation."},
                    {"series_code": "Z32", "generation_name": "300ZX Z32", "years": {"start": 1989, "end": 1996}, "body_styles": ["Coupe", "T-Bar 2+2", "Convertible"], "summary": "3.0L VG30DE and Twin-Turbo VG30DETT (208kW), Super HICAS 4-wheel steering; design masterpiece."},
                    {"series_code": "Z33", "generation_name": "350Z", "years": {"start": 2003, "end": 2009}, "body_styles": ["Coupe", "Roadster"], "summary": "3.5L VQ35DE/HR V6 (206kW-230kW), 6-speed manual, Brembo brakes; Track and Touring trims."},
                    {"series_code": "Z34", "generation_name": "370Z", "years": {"start": 2009, "end": 2021}, "body_styles": ["Coupe", "Roadster"], "summary": "3.7L VQ37VHR V6 245kW, SynchroRev Match manual transmission, NISMO variant."},
                    {"series_code": "RZ34", "generation_name": "Nissan Z", "years": {"start": 2022, "end": "Present"}, "body_styles": ["Coupe"], "summary": "3.0L VR30DDTT Twin-Turbo V6 298kW/475Nm, 6-speed manual or 9-speed auto; retro design cues."}
                ]
            },
            {
                "model_slug": "gt-r",
                "name": "GT-R",
                "vehicle_type": "Coupe",
                "segment": "Supercar",
                "years_sold_au": {"start": 2009, "end": 2022},
                "locally_built": False,
                "overview": "Nissan's standalone all-wheel-drive supercar slayer, carrying on the 'Godzilla' legacy of the R32.",
                "generations": [
                    {"series_code": "R35", "generation_name": "GT-R R35", "years": {"start": 2009, "end": 2022}, "body_styles": ["Coupe"], "summary": "Hand-built 3.8L VR38DETT Twin-Turbo V6 (357kW to 441kW NISMO), ATTESA E-TS AWD, dual-clutch transmission."}
                ]
            }
        ]
    }
]

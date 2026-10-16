"""Catalog data for Subaru, Honda, Suzuki, Isuzu, Lexus, Daihatsu, Infiniti, and Eunos in Australia."""

MAKES_PART2 = [
    {
        "make_slug": "subaru",
        "name": "Subaru",
        "country_of_origin": "Japan",
        "years_active_au": {"start": 1973, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "Subaru built a fiercely loyal following in Australia through boxer engines, symmetrical all-wheel drive, outback rally dominance, and rugged crossover utility.",
        "australian_history": """Subaru's official presence in Australia commenced in 1973 when Frank O'Brien established Subaru Motor Imports (later acquired by global automotive distributor Inchcape in 1992). The early Leone 1400 4WD wagons demonstrated that a compact passenger car could conquer Australian dirt roads and river crossings without the bulk of a heavy truck.

In 1978, Subaru introduced the Brumby (MV ute), a front-engine, selectable-4WD light utility powered by a 1.6L and later 1.8L boxer engine. The Brumby became an instant rural icon across Australian farms, sheep stations, and country towns, celebrated for its lightweight agility, incredible fuel efficiency, and near-indestructible mechanicals.

In 1989, Subaru moved upmarket with the Liberty (known globally as the Legacy), which won the prestigious Wheels Car of the Year award in 1994 and 1998. The compact Impreza arrived in 1993, followed in February 1994 by the revolutionary Impreza WRX. With a 2.0L turbocharged boxer engine and permanent symmetrical all-wheel drive, the WRX democratized supercar performance for under $40,000. New Zealander Peter 'Possum' Bourne piloted the WRX to seven consecutive Australian Rally Championship (ARC) titles from 1996 to 2002, cementing the WRX and STI as performance legends.

In 1996, Subaru created the modern crossover category with the Liberty Outback (later simply Outback), lifting the suspension and adding rugged body cladding. The Forester arrived in 1997, quickly becoming one of Australia's favourite family SUVs. In 1998, Subaru Australia made the bold decision to make All-Wheel Drive standard across its entire passenger car lineup in Australia (excluding subsequent joint-venture rear-drive coupes like the BRZ), a unique market positioning that propelled the brand to record sales. Today, Subaru Australia remains headquartered in Baulkham Hills, NSW under Inchcape Australia.""",
        "models_catalog": [
            {
                "model_slug": "brumby",
                "name": "Brumby",
                "vehicle_type": "Ute",
                "segment": "Light Commercial",
                "years_sold_au": {"start": 1978, "end": "1994"},
                "locally_built": False,
                "overview": "Cult-status compact 4WD utility loved by Australian farmers and rural communities for 16 continuous years.",
                "generations": [
                    {"series_code": "MV", "generation_name": "Brumby (AU)", "years": {"start": 1978, "end": 1994}, "body_styles": ["2-door Ute"], "summary": "1.6L EA71 and 1.8L EA81 boxer engines, selectable dual-range 4WD, rear tray jump seats in early models."}
                ]
            },
            {
                "model_slug": "liberty",
                "name": "Liberty",
                "vehicle_type": "Sedan / Wagon",
                "segment": "Mid-size Car",
                "years_sold_au": {"start": 1989, "end": "2020"},
                "locally_built": False,
                "overview": "Named Liberty specifically for Australia to avoid conflicts with Legacy clubs; multiple Wheels COTY winner.",
                "generations": [
                    {"series_code": "BC/BF", "generation_name": "Liberty 1st Gen", "years": {"start": 1989, "end": 1993}, "body_styles": ["Sedan", "Wagon"], "summary": "2.2L EJ22 boxer engine, FWD and AWD, RS Turbo rally homologation model."},
                    {"series_code": "BD/BG", "generation_name": "Liberty 2nd Gen", "years": {"start": 1994, "end": 1998}, "body_styles": ["Sedan", "Wagon"], "summary": "2.0L, 2.2L, and 2.5L EJ25 engines; Wheels COTY 1994; spawned the original Outback."},
                    {"series_code": "BE/BH", "generation_name": "Liberty 3rd Gen", "years": {"start": 1998, "end": 2003}, "body_styles": ["Sedan", "Wagon"], "summary": "Wheels COTY 1998; 2.5L 4-cylinder and 3.0L EZ30 H6 6-cylinder engine (B4 twin-turbo imported)."},
                    {"series_code": "BL/BP", "generation_name": "Liberty 4th Gen", "years": {"start": 2003, "end": 2009}, "body_styles": ["Sedan", "Wagon"], "summary": "Frameless windows, 2.0L/2.5L, 2.5L Turbo GT (180kW-194kW), 3.0R H6, and tuned by STI special editions."},
                    {"series_code": "BM/BR", "generation_name": "Liberty 5th Gen", "years": {"start": 2009, "end": 2014}, "body_styles": ["Sedan", "Wagon"], "summary": "Larger body dimensions, framed doors, 2.5L CVT, 2.5L Turbo GT, and 3.6L EZ36 H6."},
                    {"series_code": "BN/BS", "generation_name": "Liberty 6th Gen", "years": {"start": 2014, "end": 2020}, "body_styles": ["Sedan"], "summary": "Final Australian Liberty sedan; 2.5i and 3.6R H6; standard EyeSight driver assist."}
                ]
            },
            {
                "model_slug": "outback",
                "name": "Outback",
                "vehicle_type": "Crossover Wagon",
                "segment": "Large SUV / Crossover",
                "years_sold_au": {"start": 1996, "end": "Present"},
                "locally_built": False,
                "overview": "The original elevated all-wheel-drive adventure wagon, tailored for long-distance touring and country roads.",
                "generations": [
                    {"series_code": "BG", "generation_name": "Outback 1st Gen", "years": {"start": 1996, "end": 1998}, "body_styles": ["Wagon"], "summary": "Liberty-based, raised ground clearance 200mm, 2.5L EJ25 boxer, two-tone lower body cladding."},
                    {"series_code": "BH", "generation_name": "Outback 2nd Gen", "years": {"start": 1998, "end": 2003}, "body_styles": ["Wagon"], "summary": "2.5L 4-cyl and 3.0L EZ30 6-cyl (H6 3.0); VDC stability control; strong regional sales."},
                    {"series_code": "BP", "generation_name": "Outback 3rd Gen", "years": {"start": 2003, "end": 2009}, "body_styles": ["Wagon"], "summary": "2.5i, 2.5XT Turbo, and 3.0R H6; introduced 2.0L boxer turbodiesel in 2008."},
                    {"series_code": "BR", "generation_name": "Outback 4th Gen", "years": {"start": 2009, "end": 2014}, "body_styles": ["Wagon"], "summary": "Expanded interior room, 2.5i Lineartronic CVT, 2.0D diesel, 3.6R 6-cylinder."},
                    {"series_code": "BS", "generation_name": "Outback 5th Gen", "years": {"start": 2014, "end": 2020}, "body_styles": ["Wagon"], "summary": "X-Mode off-road traction, 2.5i, 2.0D diesel, 3.6R petrol; EyeSight safety standard."},
                    {"series_code": "BT", "generation_name": "Outback 6th Gen", "years": {"start": 2021, "end": "Present"}, "body_styles": ["Wagon"], "summary": "Subaru Global Platform, 2.5L direct-injected and 2.4L Turbo FA24F (183kW/350Nm); Sport, Touring, XT."}
                ]
            },
            {
                "model_slug": "forester",
                "name": "Forester",
                "vehicle_type": "SUV",
                "segment": "Medium SUV",
                "years_sold_au": {"start": 1997, "end": "Present"},
                "locally_built": False,
                "overview": "Beloved compact all-wheel-drive SUV offering wagon-like dynamics, class-leading visibility, and genuine dirt-road ability.",
                "generations": [
                    {"series_code": "SF", "generation_name": "Forester 1st Gen", "years": {"start": 1997, "end": 2002}, "body_styles": ["5-door SUV"], "summary": "2.0L EJ20 petrol and 2.0L Turbo GT (125kW); GX, Limited, GT."},
                    {"series_code": "SG", "generation_name": "Forester 2nd Gen", "years": {"start": 2002, "end": 2008}, "body_styles": ["5-door SUV"], "summary": "2.5L EJ25 and 2.5L Turbo XT (155kW-169kW); X, XS, XT; iconic bonnet scoop."},
                    {"series_code": "SH", "generation_name": "Forester 3rd Gen", "years": {"start": 2008, "end": 2013}, "body_styles": ["5-door SUV"], "summary": "Traditional SUV proportions, double-wishbone rear suspension, 2.5L petrol, 2.0L diesel, and 2.5L Turbo XT."},
                    {"series_code": "SJ", "generation_name": "Forester 4th Gen", "years": {"start": 2013, "end": 2018}, "body_styles": ["5-door SUV"], "summary": "FB25 2.5L petrol, 2.0L DIT direct-injection turbo (XT 177kW), X-Mode, EyeSight."},
                    {"series_code": "SK", "generation_name": "Forester 5th Gen", "years": {"start": 2018, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "Subaru Global Platform, 2.5L direct-injected FB25 and 2.0L e-BOXER hybrid; 2.5i, 2.5i-L, 2.5i-S, Sport."}
                ]
            },
            {
                "model_slug": "impreza",
                "name": "Impreza",
                "vehicle_type": "Hatchback / Sedan",
                "segment": "Small Car",
                "years_sold_au": {"start": 1993, "end": "Present"},
                "locally_built": False,
                "overview": "Subaru's compact passenger car and foundation for the WRX, offering standard AWD since 1998.",
                "generations": [
                    {"series_code": "GC/GF", "generation_name": "Impreza 1st Gen", "years": {"start": 1993, "end": 2000}, "body_styles": ["Sedan", "Hatchback"], "summary": "1.6L, 1.8L, and 2.0L EJ20; LX, GX, Sport; standard AWD from 1998."},
                    {"series_code": "GD/GG", "generation_name": "Impreza 2nd Gen", "years": {"start": 2000, "end": 2007}, "body_styles": ["Sedan", "Wagon"], "summary": "Bugeye (2000), Blobeye (2003), Hawkeye (2005) facelifts; 2.0L and 2.5L EJ25; 2.0i, 2.5i, RV."},
                    {"series_code": "GE/GH", "generation_name": "Impreza 3rd Gen", "years": {"start": 2007, "end": 2011}, "body_styles": ["5-door Hatch", "4-door Sedan"], "summary": "Framed windows, double-wishbone rear, 2.0L EJ20; 2.0i, RX."},
                    {"series_code": "GP/GJ", "generation_name": "Impreza 4th Gen", "years": {"start": 2011, "end": 2016}, "body_styles": ["5-door Hatch", "4-door Sedan"], "summary": "New FB20 2.0L chain-drive DOHC boxer, Lineartronic CVT, stop-start system."},
                    {"series_code": "GK/GT", "generation_name": "Impreza 5th Gen", "years": {"start": 2016, "end": 2023}, "body_styles": ["5-door Hatch", "4-door Sedan"], "summary": "First vehicle on Subaru Global Platform, 2.0L direct injection 115kW, standard EyeSight."},
                    {"series_code": "GU", "generation_name": "Impreza 6th Gen", "years": {"start": 2023, "end": "Present"}, "body_styles": ["5-door Hatch"], "summary": "Hatch-only lineup, 2.0L boxer, 11.6-inch tablet touchscreen, 2.0L, 2.0R, 2.0S."}
                ]
            },
            {
                "model_slug": "wrx",
                "name": "WRX",
                "vehicle_type": "Sedan / Hatchback / Wagon",
                "segment": "Sports Performance",
                "years_sold_au": {"start": 1994, "end": "Present"},
                "locally_built": False,
                "overview": "Rally-bred performance icon that redefined high-performance motoring in Australia with AWD grip and turbo boxer punch.",
                "generations": [
                    {"series_code": "GC8", "generation_name": "WRX 1st Gen", "years": {"start": 1994, "end": 2000}, "body_styles": ["Sedan", "Hatchback"], "summary": "EJ20G/EJ205 2.0L Turbo (155kW-160kW); Possum Bourne ARC dominator; 1999 STI official import."},
                    {"series_code": "GD/GG", "generation_name": "WRX 2nd Gen", "years": {"start": 2000, "end": 2007}, "body_styles": ["Sedan", "Wagon"], "summary": "Bugeye, Blobeye, Hawkeye; 2.0L then 2.5L EJ255 (169kW); STI with DCCD 206kW; iconic WR Blue & gold rims."},
                    {"series_code": "GE/GH/GR/GV", "generation_name": "WRX 3rd Gen", "years": {"start": 2007, "end": 2014}, "body_styles": ["Hatchback", "Sedan"], "summary": "Widebody styling from 2010; 2.5L EJ255 195kW in WRX; 2.5L EJ257 221kW in STI."},
                    {"series_code": "VA", "generation_name": "WRX 4th Gen", "years": {"start": 2014, "end": 2021}, "body_styles": ["Sedan"], "summary": "2.0L FA20F twin-scroll DIT 197kW/350Nm; WRX STI retained EJ257 221kW with hydraulic steering."},
                    {"series_code": "VB", "generation_name": "WRX 5th Gen", "years": {"start": 2022, "end": "Present"}, "body_styles": ["Sedan", "Sportswagon"], "summary": "SGP platform, 2.4L FA24F turbo boxer 202kW/350Nm; 6-speed manual or Subaru Performance Transmission."}
                ]
            },
            {
                "model_slug": "brz",
                "name": "BRZ",
                "vehicle_type": "Coupe",
                "segment": "Sports Car",
                "years_sold_au": {"start": 2012, "end": "Present"},
                "locally_built": False,
                "overview": "Pure rear-wheel-drive sports coupe co-developed with Toyota, praised for textbook chassis balance and steering feel.",
                "generations": [
                    {"series_code": "ZC6", "generation_name": "BRZ 1st Gen", "years": {"start": 2012, "end": 2021}, "body_styles": ["Coupe"], "summary": "2.0L FA20 naturally aspirated boxer 147kW/152kW, Torsen LSD, initial online-only sales sell-out."},
                    {"series_code": "ZD8", "generation_name": "BRZ 2nd Gen", "years": {"start": 2021, "end": "Present"}, "body_styles": ["Coupe"], "summary": "2.4L FA24 naturally aspirated boxer 174kW/250Nm, aluminum roof/fenders; Coupe and Coupe S."}
                ]
            }
        ]
    },
    {
        "make_slug": "honda",
        "name": "Honda",
        "country_of_origin": "Japan",
        "years_active_au": {"start": 1969, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "Celebrated for Formula 1-derived VTEC engine engineering, high-revving sports icons like the NSX, S2000, and Type R, and family benchmarks like CR-V and Civic.",
        "australian_history": """Honda's automotive presence in Australia began in 1969 when Honda Australia Pty Ltd was established in Melbourne by Colin Campbell. Early imports included the air-cooled Honda Scamp (N360/N600) and the technically advanced 1300 Coupe.

The pivotal breakthrough arrived in 1973 with the first-generation Civic. Featuring a transverse engine, independent suspension, and the low-emission CVCC clean-burn engine, the Civic was perfectly timed for the 1973 oil crisis and won acclaim for space efficiency. In 1977, the larger Accord arrived, winning the 1977 Wheels Car of the Year award. The sleek Prelude coupe followed in 1979, becoming an aspirational status symbol for young Australian urban professionals.

In 1991, Honda shook the global exotic car hierarchy with the NSX (New Sportscar eXperimental). Featuring an all-aluminium monocoque, VTEC mid-engine V6, and chassis dynamics honed at Suzuka by Formula 1 champion Ayrton Senna, the NSX challenged Ferrari in Australian showroom prestige. In 1997, Honda launched the CR-V, sparking the Australian lifestyle compact SUV revolution. The 1999 S2000 roadster pushed naturally aspirated engine engineering to 9,000 rpm with 177kW from 2.0 litres.

In 2003, the European-specification Accord Euro (CL9) won the Wheels Car of the Year award, celebrated for its razor-sharp double-wishbone chassis and slick 6-speed manual gearbox. The Jazz city car introduced clever 'Magic Seats', while Type R variants of the Integra and Civic became Australian track-day royalty. In 2021, Honda Australia transitioned from a franchised dealer model to a national agency model with unified, non-negotiable pricing. Today, Honda's Australian range focuses on Civic (including the FL5 Type R), ZR-V, CR-V, and Accord e:HEV hybrid technology.""",
        "models_catalog": [
            {
                "model_slug": "civic",
                "name": "Civic",
                "vehicle_type": "Hatchback / Sedan",
                "segment": "Small Car",
                "years_sold_au": {"start": 1973, "end": "Present"},
                "locally_built": False,
                "overview": "Honda's enduring global icon, sold in Australia across eleven generations and home to the revered Civic Type R.",
                "generations": [
                    {"series_code": "1st Gen", "generation_name": "Civic 1st Gen", "years": {"start": 1973, "end": 1979}, "body_styles": ["2-door Hatch", "4-door Sedan", "Wagon"], "summary": "1.2L EB1 and 1.5L CVCC engines, independent strut suspension, 1970s economy champion."},
                    {"series_code": "2nd/3rd Gen", "generation_name": "Civic 2nd & 3rd Gen", "years": {"start": 1979, "end": 1987}, "body_styles": ["Hatchback", "Sedan", "Shuttle Wagon"], "summary": "1.3L, 1.5L EW engines; 3rd-gen introduced flush aero styling and tall-roof Shuttle wagon."},
                    {"series_code": "4th Gen (ED/EF)", "generation_name": "Civic 4th Gen", "years": {"start": 1987, "end": 1991}, "body_styles": ["Hatchback", "Sedan"], "summary": "Double-wishbone suspension front and rear, 1.5L D15 and 1.6L D16 DOHC engines."},
                    {"series_code": "5th Gen (EG)", "generation_name": "Civic 5th Gen", "years": {"start": 1991, "end": 1995}, "body_styles": ["Hatchback", "Sedan"], "summary": "Iconic split-tailgate hatch, 1.5L and 1.6L VTEC (VTi 96kW); GL, Breeze, VTi."},
                    {"series_code": "6th Gen (EK)", "generation_name": "Civic 6th Gen", "years": {"start": 1995, "end": 2000}, "body_styles": ["Hatchback", "Sedan", "Coupe"], "summary": "1.6L D16 and 1.6L B16A2 DOHC VTEC 118kW (VTI-R); CXi, GLi, VTi, VTi-R."},
                    {"series_code": "7th Gen (EU/ES)", "generation_name": "Civic 7th Gen", "years": {"start": 2000, "end": 2005}, "body_styles": ["5-door Hatch", "4-door Sedan"], "summary": "Dashboard-mounted gearshift, MacPherson front suspension, 1.7L D17 engine."},
                    {"series_code": "8th Gen (FD/FN2)", "generation_name": "Civic 8th Gen", "years": {"start": 2006, "end": 2011}, "body_styles": ["4-door Sedan", "3-door Hatch (Type R)"], "summary": "Two-tier digital instrument dash, 1.8L and 2.0L; UK-built FN2 Type R 2.0L K20Z4 148kW."},
                    {"series_code": "9th Gen (FB/FK)", "generation_name": "Civic 9th Gen", "years": {"start": 2012, "end": 2016}, "body_styles": ["Hatchback", "Sedan"], "summary": "1.8L and 2.0L i-VTEC, VTi, VTi-L, VTi-S, Sport."},
                    {"series_code": "10th Gen (FC/FK)", "generation_name": "Civic 10th Gen", "years": {"start": 2016, "end": 2021}, "body_styles": ["Hatchback", "Sedan"], "summary": "1.5L Turbo VTEC (127kW) and FK8 Type R with 2.0L Turbo K20C1 (228kW/400Nm)."},
                    {"series_code": "11th Gen (FL)", "generation_name": "Civic 11th Gen", "years": {"start": 2021, "end": "Present"}, "body_styles": ["Hatchback"], "summary": "Premium cabin, e:HEV hybrid powertrain and world-class FL5 Civic Type R 2.0L Turbo 235kW."}
                ]
            },
            {
                "model_slug": "accord-euro",
                "name": "Accord Euro",
                "vehicle_type": "Sedan",
                "segment": "Mid-size Car",
                "years_sold_au": {"start": 2003, "end": "2015"},
                "locally_built": False,
                "overview": "European-engineered sports sedan celebrated for benchmark double-wishbone chassis and tactile 6-speed manual; Wheels COTY 2003.",
                "generations": [
                    {"series_code": "CL9", "generation_name": "Accord Euro 1st Gen", "years": {"start": 2003, "end": 2008}, "body_styles": ["Sedan"], "summary": "2.4L K24A3 i-VTEC engine 140kW, 6-speed manual or 5-speed auto, Wheels COTY 2003."},
                    {"series_code": "CU2", "generation_name": "Accord Euro 2nd Gen", "years": {"start": 2008, "end": 2015}, "body_styles": ["Sedan"], "summary": "Wider track, 2.4L K24Z3 148kW, standard/Luxury/Luxury Navi grades; final European Accord."}
                ]
            },
            {
                "model_slug": "cr-v",
                "name": "CR-V",
                "vehicle_type": "SUV",
                "segment": "Medium SUV",
                "years_sold_au": {"start": 1997, "end": "Present"},
                "locally_built": False,
                "overview": "The vehicle that ignited Australia's lifestyle compact SUV revolution, complete with an in-floor picnic table in early models.",
                "generations": [
                    {"series_code": "RD1-RD3", "generation_name": "CR-V 1st Gen", "years": {"start": 1997, "end": 2001}, "body_styles": ["5-door SUV"], "summary": "2.0L B20B/B20Z engine, Real Time 4WD, flat cabin floor, folding picnic table in boot."},
                    {"series_code": "RD4-RD7", "generation_name": "CR-V 2nd Gen", "years": {"start": 2001, "end": 2006}, "body_styles": ["5-door SUV"], "summary": "2.4L K24A1 i-VTEC engine 118kW, increased cargo space, dash-mounted handbrake."},
                    {"series_code": "RE", "generation_name": "CR-V 3rd Gen", "years": {"start": 2006, "end": 2012}, "body_styles": ["5-door SUV"], "summary": "Lower center of gravity, tailgate opening upward instead of outward, 2.4L K24Z 125kW."},
                    {"series_code": "RM", "generation_name": "CR-V 4th Gen", "years": {"start": 2012, "end": 2017}, "body_styles": ["5-door SUV"], "summary": "Offered in 2WD and AWD, 2.0L and 2.4L petrol, plus 1.6L/2.2L i-DTEC diesel."},
                    {"series_code": "RW", "generation_name": "CR-V 5th Gen", "years": {"start": 2017, "end": 2023}, "body_styles": ["5-door SUV"], "summary": "1.5L VTEC Turbo (140kW), available 7 seats, Honda Sensing safety suite."},
                    {"series_code": "RS", "generation_name": "CR-V 6th Gen", "years": {"start": 2023, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "1.5L Turbo petrol and 2.0L two-motor e:HEV hybrid; VTi X, VTi L, e:HEV RS."}
                ]
            },
            {
                "model_slug": "s2000",
                "name": "S2000",
                "vehicle_type": "Roadster Convertible",
                "segment": "Sports Car",
                "years_sold_au": {"start": 1999, "end": "2008"},
                "locally_built": False,
                "overview": "Pure naturally aspirated roadster celebrating Honda's 50th anniversary, featuring the F20C engine revving to 9,000 rpm.",
                "generations": [
                    {"series_code": "AP1/AP2", "generation_name": "S2000", "years": {"start": 1999, "end": 2008}, "body_styles": ["Roadster Convertible"], "summary": "2.0L F20C DOHC VTEC producing 177kW at 8,300rpm, 50:50 weight distribution, X-bone frame."}
                ]
            },
            {
                "model_slug": "nsx",
                "name": "NSX",
                "vehicle_type": "Coupe",
                "segment": "Supercar",
                "years_sold_au": {"start": 1991, "end": "2020"},
                "locally_built": False,
                "overview": "Mid-engine supercar that reset exotic car engineering standards with Ayrton Senna chassis development.",
                "generations": [
                    {"series_code": "NA1/NA2", "generation_name": "NSX 1st Gen", "years": {"start": 1991, "end": 2002}, "body_styles": ["Coupe", "Targa"], "summary": "All-aluminum monocoque, 3.0L C30A (201kW) then 3.2L C32B (206kW) VTEC V6, 6-speed manual."},
                    {"series_code": "NC1", "generation_name": "NSX 2nd Gen", "years": {"start": 2016, "end": 2020}, "body_styles": ["Coupe"], "summary": "3.5L Twin-Turbo V6 with three electric motors (Sport Hybrid SH-AWD) generating 427kW."}
                ]
            },
            {
                "model_slug": "jazz",
                "name": "Jazz",
                "vehicle_type": "Hatchback",
                "segment": "Light Car",
                "years_sold_au": {"start": 2002, "end": "2021"},
                "locally_built": False,
                "overview": "Masterclass in interior packaging, renowned for its Magic Seats that allowed tall objects or flat camping beds inside a micro footprint.",
                "generations": [
                    {"series_code": "GD", "generation_name": "Jazz 1st Gen", "years": {"start": 2002, "end": 2008}, "body_styles": ["5-door Hatch"], "summary": "Center-mounted fuel tank, Magic Seats, 1.3L i-DSI and 1.5L VTEC engines; GLi, VTi, VTi-S."},
                    {"series_code": "GE", "generation_name": "Jazz 2nd Gen", "years": {"start": 2008, "end": 2014}, "body_styles": ["5-door Hatch"], "summary": "Expanded cabin, 1.3L and 1.5L i-VTEC, 5-speed auto/manual, introduced Jazz Hybrid in 2013."},
                    {"series_code": "GK", "generation_name": "Jazz 3rd Gen", "years": {"start": 2014, "end": 2021}, "body_styles": ["5-door Hatch"], "summary": "1.5L direct-injected L15B engine 88kW, CVT automatic, final Jazz model sold in Australia."}
                ]
            }
        ]
    },
    {
        "make_slug": "suzuki",
        "name": "Suzuki",
        "country_of_origin": "Japan",
        "years_active_au": {"start": 1974, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "Masters of lightweight 4x4s, cheerful hatchbacks, and cult oddities like the Mighty Boy. Celebrated for Jimny, Swift GTi, and Vitara.",
        "australian_history": """Suzuki's Australian adventure kicked off in 1974 with the importation of lightweight 4x4 vehicles by Mayne Nickless and regional distributors like MW Suzuki in Queensland. The tiny two-stroke LJ50 4WD immediately gained a cult following for its ability to float over soft coastal sand dunes and scramble up rock trails where heavy trucks got bogged.

In 1981, Suzuki introduced the Sierra (SJ410/SJ413), a ladder-chassis, dual-range 4WD that became an Australian icon. Lightweight, cheap to run, and endlessly customizable, the Sierra introduced thousands of young Australians to four-wheel driving. In 1985, Suzuki launched the Mighty Boy, a 543cc, front-wheel-drive micro-ute. Classified as a commercial vehicle with lower tariffs, the Mighty Boy became a quirky Aussie pop-culture legend.

In the small car arena, Suzuki struck gold in 1986 with the Swift GTi. Packing a 1.3L DOHC 16-valve engine revving to 7,500 rpm into a sub-800kg hatchback, the GTi became the quintessential giant-killer on road and rally stages. Through a long-running joint venture with General Motors, Suzuki's Swift was also assembled and sold in Australia as the Holden Barina (MB through MH series) from 1985 to 1994, winning Wheels Car of the Year in 1985.

In 1988, Suzuki created the compact lifestyle 4WD class with the Vitara, combining coil-spring road comfort with dual-range off-road hardware. In 1998, the Jimny replaced the Sierra, maintaining a live-axle ladder chassis while modernizing safety. The 2018 fourth-generation Jimny (JB74) ignited unprecedented demand in Australia, with waitlists stretching beyond two years. Today, Suzuki Australia operates through Suzuki Australia (eastern states) and independent distributor MW Suzuki (Western Australia).""",
        "models_catalog": [
            {
                "model_slug": "jimny",
                "name": "Jimny",
                "vehicle_type": "4WD SUV",
                "segment": "Compact 4WD",
                "years_sold_au": {"start": 1998, "end": "Present"},
                "locally_built": False,
                "overview": "The world's purest mini off-roader: separate ladder chassis, live axles front and rear, and dual-range 4WD.",
                "generations": [
                    {"series_code": "JB23/JB43", "generation_name": "Jimny 3rd Gen", "years": {"start": 1998, "end": 2018}, "body_styles": ["3-door Hardtop", "Cabrio Soft-top"], "summary": "1.3L G13BB then M13A engine, coil springs, vacuum-locking hubs; 20-year Australian sales run."},
                    {"series_code": "JB64/JB74/JC74", "generation_name": "Jimny 4th Gen", "years": {"start": 2018, "end": "Present"}, "body_styles": ["3-door 4WD", "5-door XL 4WD"], "summary": "Retro boxy styling, 1.5L K15B engine, AllGrip Pro 4WD; 3-door Jimny and 5-door Jimny XL."}
                ]
            },
            {
                "model_slug": "sierra",
                "name": "Sierra",
                "vehicle_type": "4WD SUV / Ute",
                "segment": "Compact 4WD",
                "years_sold_au": {"start": 1981, "end": "1999"},
                "locally_built": False,
                "overview": "Australian bush legend, famous for lightweight rock climbing, beach running, and unstoppable off-road tenacity.",
                "generations": [
                    {"series_code": "SJ410/SJ413", "generation_name": "Sierra", "years": {"start": 1981, "end": 1999}, "body_styles": ["Soft-top", "Hardtop", "Long Wheelbase Ute"], "summary": "1.0L F10A and 1.3L G13A/BA engines, dual-range transfer case, leaf springs, LWB tray-back ute."}
                ]
            },
            {
                "model_slug": "mighty-boy",
                "name": "Mighty Boy",
                "vehicle_type": "Micro Ute",
                "segment": "Kei Commercial",
                "years_sold_au": {"start": 1985, "end": "1988"},
                "locally_built": False,
                "overview": "Australia's smallest production ute, a 543cc front-wheel-drive cult hero with a 550kg kerb weight.",
                "generations": [
                    {"series_code": "SS40T", "generation_name": "Mighty Boy", "years": {"start": 1985, "end": 1988}, "body_styles": ["2-door Micro Ute"], "summary": "543cc F5A 3-cylinder engine (21kW), 4-speed manual or 2-speed automatic, iconic Aussie cult classic."}
                ]
            },
            {
                "model_slug": "swift",
                "name": "Swift",
                "vehicle_type": "Hatchback / Sedan",
                "segment": "Light Car",
                "years_sold_au": {"start": 1984, "end": "Present"},
                "locally_built": False,
                "overview": "Australia's favourite pocket rocket in GTi trim, and later a stylish, fun-to-drive world hatchback.",
                "generations": [
                    {"series_code": "SA/AA", "generation_name": "Swift 1st Gen", "years": {"start": 1984, "end": 1989}, "body_styles": ["3-door Hatch", "5-door Hatch"], "summary": "1.0L 3-cyl and 1.3L 4-cyl; basis for Holden Barina MB/ML (Wheels COTY 1985); first GTi in 1986."},
                    {"series_code": "SF", "generation_name": "Swift 2nd Gen", "years": {"start": 1989, "end": 2000}, "body_styles": ["Hatchback", "Sedan", "Convertible"], "summary": "Legendary Swift GTi with 1.3L DOHC 16V G13B 74kW at 7,500rpm in an 810kg body."},
                    {"series_code": "RS/ZC21", "generation_name": "Swift 3rd Gen (World Car)", "years": {"start": 2005, "end": 2011}, "body_styles": ["5-door Hatch"], "summary": "European-inspired styling, 1.5L M15A and Swift Sport 1.6L M16A (92kW); huge sales success."},
                    {"series_code": "FZ/ZC32", "generation_name": "Swift 4th Gen", "years": {"start": 2011, "end": 2017}, "body_styles": ["5-door Hatch"], "summary": "1.4L K14B petrol and Swift Sport 1.6L M16A 100kW with 6-speed manual."},
                    {"series_code": "AZ/ZC33", "generation_name": "Swift 5th Gen", "years": {"start": 2017, "end": "Present"}, "body_styles": ["5-door Hatch"], "summary": "Heartect platform, 1.2L Dualjet, 1.0L Boosterjet turbo, and 1.4L Boosterjet Turbo Swift Sport (103kW/230Nm)."}
                ]
            },
            {
                "model_slug": "vitara",
                "name": "Vitara",
                "vehicle_type": "SUV",
                "segment": "Compact / Small SUV",
                "years_sold_au": {"start": 1988, "end": "Present"},
                "locally_built": False,
                "overview": "The pioneer of the compact lifestyle 4WD, evolving into the rugged Grand Vitara and modern crossover.",
                "generations": [
                    {"series_code": "ET/TA", "generation_name": "Vitara 1st Gen", "years": {"start": 1988, "end": 1998}, "body_styles": ["SWB Soft/Hardtop", "LWB 5-door"], "summary": "1.6L G16A/B petrol, 2.0L V6 in 5-door, separate ladder chassis with dual-range 4WD."},
                    {"series_code": "FT/GT", "generation_name": "Grand Vitara 2nd Gen", "years": {"start": 1998, "end": 2005}, "body_styles": ["3-door SUV", "5-door SUV", "XL-7 7-seater"], "summary": "1.6L, 2.0L, 2.5L V6, and 2.7L V6 in stretched 7-seat XL-7; dual-range 4WD."},
                    {"series_code": "JT", "generation_name": "Grand Vitara 3rd Gen", "years": {"start": 2005, "end": 2014}, "body_styles": ["3-door SUV", "5-door SUV"], "summary": "Built-in ladder frame monocoque, IRS, 2.4L 4-cylinder, 2.7L/3.2L V6, and 1.9L diesel."},
                    {"series_code": "LY", "generation_name": "Vitara 4th Gen", "years": {"start": 2015, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "Monocoque crossover, 1.6L naturally aspirated and 1.4L Boosterjet turbo (AllGrip AWD)."}
                ]
            }
        ]
    },
    {
        "make_slug": "isuzu",
        "name": "Isuzu / Isuzu UTE",
        "country_of_origin": "Japan",
        "years_active_au": {"start": 1971, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "From providing the foundation for the Holden Gemini and Holden Rodeo to dominating Australian ute and SUV sales with the D-MAX and MU-X.",
        "australian_history": """Isuzu's history in Australia began in the mid-1960s with small-scale imports of the Bellett and Florian sedans. The brand's true impact arrived in 1971 when General Motors acquired a 34% stake in Isuzu Japan, initiating a four-decade engineering partnership with General Motors-Holden in Australia.

In 1975, Holden adapted the Isuzu Gemini (T-car) to create the beloved Holden Gemini (TX-TG series), manufactured at Holden's Acacia Ridge plant in Brisbane. The Gemini became Australia's favourite 4-cylinder car for a decade. Holden also relied entirely on Isuzu for its commercial vehicles: the Isuzu KB became the Holden Rodeo in 1980, followed by the TF Rodeo in 1988 and RA Rodeo in 2003, which became staples of the Australian building trades and farming sectors. Similarly, the Isuzu Trooper was marketed as the Holden Jackaroo from 1981 to 2003.

When GM and Isuzu ended their light-commercial joint venture in 2008, Isuzu established Isuzu UTE Australia (IUA) as an independent factory distributor headquartered in Brisbane. IUA launched the D-MAX utility in 2008, powered by the legendary 3.0L 4JJ1 commercial truck-derived turbo-diesel engine. Renowned for cast-iron cylinder block durability, timing chain reliability, and effortless towing, the D-MAX earned unmatched trust among outback caravanners and trades.

In 2013, IUA launched the MU-X, a 7-seat 4WD wagon based on the D-MAX chassis. The MU-X became Australia's #1 selling ute-based SUV outside Toyota. In 2020, the third-generation D-MAX and second-generation MU-X arrived, introducing standard 5-star ANCAP safety, advanced driver assist systems (IDAS), and the refined 4JJ3-TCX engine, consistently ranking among Australia's top three best-selling utes.""",
        "models_catalog": [
            {
                "model_slug": "d-max",
                "name": "D-MAX",
                "vehicle_type": "Ute / Cab Chassis",
                "segment": "Light Commercial",
                "years_sold_au": {"start": 2008, "end": "Present"},
                "locally_built": False,
                "overview": "Isuzu UTE's powerhouse dual-cab and single-cab ute, revered across Australia for the legendary 3.0L 4JJ1/4JJ3 diesel engine.",
                "generations": [
                    {"series_code": "RA/RC", "generation_name": "D-MAX 1st Gen (AU)", "years": {"start": 2008, "end": 2012}, "body_styles": ["Single Cab", "Space Cab", "Crew Cab"], "summary": "3.0L 4JJ1-TC turbo-diesel 120kW/360Nm, dual-range 4WD, 3000kg towing; EX, SX, LS, LS-M, LS-U."},
                    {"series_code": "RT50/RT85", "generation_name": "D-MAX 2nd Gen", "years": {"start": 2012, "end": 2020}, "body_styles": ["Single Cab", "Space Cab", "Crew Cab"], "summary": "Updated 4JJ1-TC-Hi-Power (130kW/430Nm), 3500kg towing, coil-spring front suspension; SX, LS-M, LS-U, LS-T, X-Runner."},
                    {"series_code": "RG01", "generation_name": "D-MAX 3rd Gen", "years": {"start": 2020, "end": "Present"}, "body_styles": ["Single Cab", "Space Cab", "Crew Cab"], "summary": "3.0L 4JJ3-TCX (140kW/450Nm) and 1.9L RZ4E-TC diesel; 5-star ANCAP IDAS; SX, LS-M, LS-U, LS-U+, X-Terrain."}
                ]
            },
            {
                "model_slug": "mu-x",
                "name": "MU-X",
                "vehicle_type": "SUV",
                "segment": "Large 4WD SUV",
                "years_sold_au": {"start": 2013, "end": "Present"},
                "locally_built": False,
                "overview": "D-MAX-based 7-seat 4WD wagon featuring multi-link rear coil suspension, Australia's favourite caravan hauler.",
                "generations": [
                    {"series_code": "RF10/RF20", "generation_name": "MU-X 1st Gen", "years": {"start": 2013, "end": 2021}, "body_styles": ["5-door Wagon (7 seats)"], "summary": "3.0L 4JJ1 turbo-diesel 130kW/430Nm, 5-speed then 6-speed auto, 3000kg towing; LS-M, LS-U, LS-T."},
                    {"series_code": "RJ01", "generation_name": "MU-X 2nd Gen", "years": {"start": 2021, "end": "Present"}, "body_styles": ["5-door Wagon (7 seats)"], "summary": "3.0L 4JJ3-TCX (140kW/450Nm) and 1.9L diesel, 3500kg towing, rear differential lock; LS-M, LS-U, LS-T."}
                ]
            }
        ]
    },
    {
        "make_slug": "lexus",
        "name": "Lexus",
        "country_of_origin": "Japan",
        "years_active_au": {"start": 1990, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "Toyota's luxury division launched in Australia in May 1990, redefining premium ownership through obsessive build quality, hybrid technology, and the Lexus Encore service program.",
        "australian_history": """Lexus officially entered the Australian luxury vehicle market in May 1990 with a single, devastatingly refined model: the LS400 flagship sedan. Engineered under the 'Circle F' program at a cost of over $1 billion USD, the LS400 featured an acoustically silent 4.0L 1UZ-FE quad-cam V8 and tolerances so precise that it stunned the German luxury establishment.

Complementing the vehicle's engineering was the Lexus Encore Privileges program, which introduced Australian luxury buyers to complimentary pickup and delivery for servicing, loan cars, golf days, and opera sponsorships, setting a new benchmark for customer care.

In 1992, Lexus expanded with the ES300 mid-size sedan, followed in 1997 by the GS300 executive sports sedan. In 1998, Lexus launched its first luxury 4WD, the LX470, combining the bulletproof underpinnings of the LandCruiser 100 with hydraulic suspension and opulent Connolly leather. In 1999, the compact IS200 arrived to challenge the BMW 3 Series.

In 2003, Lexus introduced the RX330 luxury SUV, which rapidly became the brand's volume backbone in Australia. In 2006, Lexus pioneered luxury hybrid motoring in Australia with the RX400h and GS450h. In 2007, Lexus launched the high-performance 'F' brand with the IS F, packing a 5.0L 2UR-GSE V8 with 311kW. In 2011, Australia received fewer than 10 allocations of the carbon-fibre LFA V10 supercar, priced over $700,000. Today, Lexus Australia commands strong luxury market share led by the NX, RX, and UX hybrid and electric SUVs.""",
        "models_catalog": [
            {
                "model_slug": "ls",
                "name": "LS",
                "vehicle_type": "Sedan",
                "segment": "Upper Large Luxury",
                "years_sold_au": {"start": 1990, "end": "Present"},
                "locally_built": False,
                "overview": "The original Japanese flagship that disrupted the global luxury market in 1990 with the whispering 1UZ-FE V8.",
                "generations": [
                    {"series_code": "XF10", "generation_name": "LS400 1st Gen", "years": {"start": 1990, "end": 1994}, "body_styles": ["Sedan"], "summary": "4.0L 1UZ-FE V8 190kW, 4-speed auto, pioneering NVH reduction, established Lexus in Australia."},
                    {"series_code": "XF20", "generation_name": "LS400 2nd Gen", "years": {"start": 1994, "end": 2000}, "body_styles": ["Sedan"], "summary": "4.0L V8 updated with VVT-i (216kW), 5-speed auto, increased rear legroom."},
                    {"series_code": "XF30", "generation_name": "LS430 3rd Gen", "years": {"start": 2000, "end": 2006}, "body_styles": ["Sedan"], "summary": "4.3L 3UZ-FE V8 207kW, radar cruise control, soft-close doors, Mark Levinson audio."},
                    {"series_code": "XF40", "generation_name": "LS460 / LS600h 4th Gen", "years": {"start": 2006, "end": 2017}, "body_styles": ["Sedan", "LWB Sedan"], "summary": "4.6L 1UR-FSE V8 (285kW) and world-first V8 hybrid LS600hL (5.0L 2UR-FSE AWD 327kW)."},
                    {"series_code": "XF50", "generation_name": "LS500 / LS500h 5th Gen", "years": {"start": 2017, "end": "Present"}, "body_styles": ["Sedan"], "summary": "GA-L platform, 3.5L Twin-Turbo V6 (V35A-FTS 310kW) and 3.5L Multi-Stage Hybrid."}
                ]
            },
            {
                "model_slug": "is",
                "name": "IS",
                "vehicle_type": "Sedan",
                "segment": "Compact Luxury Sedan",
                "years_sold_au": {"start": 1999, "end": "2021"},
                "locally_built": False,
                "overview": "Rear-wheel-drive compact sports sedan famous for chronograph instruments, the V8 IS F, and agile dynamics.",
                "generations": [
                    {"series_code": "XE10", "generation_name": "IS200 / IS300 1st Gen", "years": {"start": 1999, "end": 2005}, "body_styles": ["Sedan"], "summary": "2.0L 1G-FE inline-6 and 3.0L 2JZ-GE inline-6, chronograph watch-dial instruments."},
                    {"series_code": "XE20", "generation_name": "IS250 / IS F 2nd Gen", "years": {"start": 2005, "end": 2013}, "body_styles": ["Sedan", "Convertible (IS250C)"], "summary": "2.5L 4GR-FSE V6, 3.5L 2GR-FSE; 5.0L V8 IS F (311kW) high-performance hero in 2008."},
                    {"series_code": "XE30", "generation_name": "IS300 / IS350 3rd Gen", "years": {"start": 2013, "end": 2021}, "body_styles": ["Sedan"], "summary": "Spindle grille styling, 2.0L Turbo (IS300), 2.5L Hybrid (IS300h), and 3.5L V6 (IS350 232kW)."}
                ]
            },
            {
                "model_slug": "rx",
                "name": "RX",
                "vehicle_type": "SUV",
                "segment": "Medium / Large Luxury SUV",
                "years_sold_au": {"start": 2003, "end": "Present"},
                "locally_built": False,
                "overview": "Lexus's most successful model in Australia, pioneering luxury crossover comfort and hybrid efficiency.",
                "generations": [
                    {"series_code": "XU30", "generation_name": "RX 2nd Gen (1st in AU)", "years": {"start": 2003, "end": 2009}, "body_styles": ["5-door SUV"], "summary": "3.3L 3MZ-FE V6 (RX330) and 2006 RX400h hybrid (Australia's first luxury hybrid SUV)."},
                    {"series_code": "AL10", "generation_name": "RX 3rd Gen", "years": {"start": 2009, "end": 2015}, "body_styles": ["5-door SUV"], "summary": "3.5L 2GR-FE V6 (RX350) and Atkinson-cycle hybrid (RX450h), Remote Touch controller."},
                    {"series_code": "AL20", "generation_name": "RX 4th Gen", "years": {"start": 2015, "end": 2022}, "body_styles": ["5-door SUV", "7-seat RX L"], "summary": "Angular sharp styling, 2.0L Turbo (RX300), 3.5L V6, 3.5L Hybrid; available 7-seat RX L."},
                    {"series_code": "AL30", "generation_name": "RX 5th Gen", "years": {"start": 2022, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "GA-K platform, RX350 (2.4L Turbo), RX350h, RX450h+ PHEV, and performance RX500h F Sport Performance (273kW)."}
                ]
            },
            {
                "model_slug": "nx",
                "name": "NX",
                "vehicle_type": "SUV",
                "segment": "Medium Luxury SUV",
                "years_sold_au": {"start": 2014, "end": "Present"},
                "locally_built": False,
                "overview": "Mid-size luxury crossover that quickly became Lexus's top-selling model line in Australia.",
                "generations": [
                    {"series_code": "AZ10", "generation_name": "NX 1st Gen", "years": {"start": 2014, "end": 2021}, "body_styles": ["5-door SUV"], "summary": "2.0L Turbo 8AR-FTS (NX200t/NX300) and 2.5L Hybrid (NX300h); Luxury, F Sport, Sports Luxury."},
                    {"series_code": "AZ20", "generation_name": "NX 2nd Gen", "years": {"start": 2021, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "GA-K platform, NX250, NX350 2.4L Turbo AWD, NX350h Hybrid, and NX450h+ Plug-in Hybrid (227kW)."}
                ]
            },
            {
                "model_slug": "lx",
                "name": "LX",
                "vehicle_type": "4WD SUV",
                "segment": "Upper Large Luxury 4WD",
                "years_sold_au": {"start": 1996, "end": "Present"},
                "locally_built": False,
                "overview": "Pinnacle luxury 4WD based on the Toyota LandCruiser, combining ultimate off-road durability with first-class opulence.",
                "generations": [
                    {"series_code": "FZJ80", "generation_name": "LX450", "years": {"start": 1996, "end": 1998}, "body_styles": ["5-door 4WD"], "summary": "LandCruiser 80-based, 4.5L 1FZ-FE inline-6 petrol, leather and walnut trim."},
                    {"series_code": "UZJ100", "generation_name": "LX470", "years": {"start": 1998, "end": 2007}, "body_styles": ["5-door 4WD"], "summary": "LandCruiser 100-based, 4.7L 2UZ-FE V8, Adaptive Variable Suspension with Active Height Control."},
                    {"series_code": "URJ200", "generation_name": "LX570", "years": {"start": 2008, "end": 2021}, "body_styles": ["5-door 4WD"], "summary": "5.7L 3UR-FE V8 (270kW/530Nm) and 2018 LX450d with 4.5L Twin-Turbo V8 diesel (200kW/650Nm)."},
                    {"series_code": "J310", "generation_name": "LX500d / LX600", "years": {"start": 2022, "end": "Present"}, "body_styles": ["5-door 4WD"], "summary": "TNGA-F platform, 3.3L Twin-Turbo V6 diesel (LX500d 227kW) and 3.5L Twin-Turbo V6 petrol (LX600 305kW); 4-seat Ultra Luxury VIP."}
                ]
            }
        ]
    },
    {
        "make_slug": "daihatsu",
        "name": "Daihatsu",
        "country_of_origin": "Japan",
        "years_active_au": {"start": 1967, "end": 2006},
        "currently_sold_au": False,
        "local_manufacturer": False,
        "overview": "Pioneers of compact 3-cylinder economy cars and nimble mini-4x4s, beloved for the Charade, Rocky, and Feroza.",
        "australian_history": """Daihatsu arrived in Australia in 1967 with the Compagno 800 and 1000 range of sedans, wagons, and utilities. In 1977, Daihatsu launched the G10 Charade, powered by an innovative 993cc 3-cylinder engine. The Charade was hailed for its exceptional packaging and fuel efficiency, winning the 1979 Wheels Car of the Year award.

Throughout the 1980s, the Charade became one of Australia's most popular first cars. In 1988, Daihatsu brought the hot-hatch world the Charade GTti, boasting a 1.0L twin-cam intercooled turbo 3-cylinder (CB70/CB80) producing 74kW and revving to 9,000 rpm. The Handivan and Mira delivery vans also carved out a major niche in Australian metropolitan courier fleets.

In the off-road arena, Daihatsu earned immense respect with the Rocky (F70/F75/F80) and Feroza (F300), offering genuine dual-range four-wheel drive and tough ladder-chassis engineering in a compact footprint. In 2000, Toyota acquired a controlling interest in Daihatsu. Facing tightening margins in the light car segment and Toyota's decision to streamline its small-car strategy around the Echo and Yaris, Daihatsu officially withdrew from the Australian new car market in March 2006.""",
        "models_catalog": [
            {
                "model_slug": "charade",
                "name": "Charade",
                "vehicle_type": "Hatchback / Sedan",
                "segment": "Light Car",
                "years_sold_au": {"start": 1977, "end": 2006},
                "locally_built": False,
                "overview": "Australia's favourite 3-cylinder city runabout, Wheels COTY 1979 winner, and GTti pocket rocket.",
                "generations": [
                    {"series_code": "G10", "generation_name": "Charade 1st Gen", "years": {"start": 1977, "end": 1983}, "body_styles": ["3-door Hatch", "5-door Hatch"], "summary": "993cc 3-cylinder CB20 engine, round opera windows on 3-door; Wheels COTY 1979."},
                    {"series_code": "G11", "generation_name": "Charade 2nd Gen", "years": {"start": 1983, "end": 1987}, "body_styles": ["3-door Hatch", "5-door Hatch"], "summary": "1.0L petrol and 1.0L CL diesel; first Charade Turbo model introduced in 1984."},
                    {"series_code": "G100", "generation_name": "Charade 3rd Gen", "years": {"start": 1987, "end": 1993}, "body_styles": ["3-door Hatch", "5-door Hatch", "Sedan"], "summary": "1.0L 3-cyl and 1.3L 4-cyl; GTti hot hatch with 74kW twin-cam turbo revving to 9000rpm."},
                    {"series_code": "G200", "generation_name": "Charade 4th Gen", "years": {"start": 1993, "end": 2000}, "body_styles": ["3-door Hatch", "5-door Hatch", "Sedan"], "summary": "1.3L and 1.5L 4-cylinder engines; Centro and Detomaso sports editions."},
                    {"series_code": "XP40", "generation_name": "Charade 5th Gen (AU)", "years": {"start": 2003, "end": 2006}, "body_styles": ["3-door Hatch", "5-door Hatch"], "summary": "Daihatsu Mira/Toyota Echo-based 1.0L 3-cylinder budget city car; final Charade in Australia."}
                ]
            },
            {
                "model_slug": "feroza",
                "name": "Feroza",
                "vehicle_type": "4WD SUV",
                "segment": "Compact 4WD",
                "years_sold_au": {"start": 1988, "end": "1998"},
                "locally_built": False,
                "overview": "Rugged, removable-hardtop mini 4x4 with independent front suspension and dual-range 4WD.",
                "generations": [
                    {"series_code": "F300", "generation_name": "Feroza", "years": {"start": 1988, "end": 1998}, "body_styles": ["2-door Hardtop", "Soft-top"], "summary": "1.6L HD-C (carb) then HD-E (EFI) petrol, dual-range transfer case, torsion-bar front and leaf rear."}
                ]
            },
            {
                "model_slug": "rocky",
                "name": "Rocky",
                "vehicle_type": "4WD SUV / Ute",
                "segment": "Compact 4WD",
                "years_sold_au": {"start": 1984, "end": "1998"},
                "locally_built": False,
                "overview": "Heavy-duty diesel compact 4WD with solid beam axles front and rear, celebrated for tractor-like outback resilience.",
                "generations": [
                    {"series_code": "F70/F75/F80", "generation_name": "Rocky", "years": {"start": 1984, "end": 1998}, "body_styles": ["SWB Hardtop", "LWB Wagon", "Cab Chassis Ute"], "summary": "2.8L DL naturally aspirated and DL-T turbo-diesel engines; beam axles and leaf springs."}
                ]
            },
            {
                "model_slug": "copen",
                "name": "Copen",
                "vehicle_type": "Roadster",
                "segment": "Micro Sports",
                "years_sold_au": {"start": 2003, "end": "2006"},
                "locally_built": False,
                "overview": "Charming two-seat roadster featuring an electric retractable aluminum hardtop.",
                "generations": [
                    {"series_code": "L880", "generation_name": "Copen", "years": {"start": 2003, "end": 2006}, "body_styles": ["Retractable Hardtop Roadster"], "summary": "659cc JB-DET 4-cylinder turbo in initial batch, followed by 1.3L K3-VE 4-cylinder engine."}
                ]
            }
        ]
    },
    {
        "make_slug": "infiniti",
        "name": "Infiniti",
        "country_of_origin": "Japan",
        "years_active_au": {"start": 2012, "end": 2020},
        "currently_sold_au": False,
        "local_manufacturer": False,
        "overview": "Nissan's premium performance division sold rear-wheel-drive luxury sedans, coupes, and SUVs through flagship retail centers in Australia.",
        "australian_history": """Nissan initially tested the Australian luxury market in 1993 with a small batch of Infiniti Q45 flagships sold via select Nissan dealerships. In September 2012, Nissan officially launched Infiniti as a standalone brand in Australia, investing tens of millions in lavish 'Infiniti Centers' in Sydney, Melbourne, and Brisbane.

The launch range showcased performance rear-drive and all-wheel-drive platforms: the FX luxury crossover (FX37 V6, FX50 290kW 5.0L V8, and FX30d V6 diesel), the M luxury sedan (M37, M56 V8, and M35h hybrid), and the G37 sports coupe and convertible. In 2014, Infiniti adopted the Q/QX naming convention and launched the Q50 mid-size sports sedan, which introduced steer-by-wire Direct Adaptive Steering.

In 2016, Infiniti introduced the Mercedes-Benz GLA-based Q30 hatchback and QX30 crossover, alongside the massive 5.6L V8 QX80 4WD wagon. Despite praise for styling and powertrain performance (notably the 298kW VR30 twin-turbo V6 in the Q50 Red Sport and Q60 Red Sport), brand recognition remained low against entrenched European marques. In September 2019, Infiniti announced its withdrawal from Western Europe and Australia, officially closing sales in late 2020 with Nissan Australia assuming long-term warranty and parts support.""",
        "models_catalog": [
            {
                "model_slug": "q50",
                "name": "Q50",
                "vehicle_type": "Sedan",
                "segment": "Medium Luxury Sedan",
                "years_sold_au": {"start": 2014, "end": 2020},
                "locally_built": False,
                "overview": "Rear-wheel-drive sports sedan featuring world-first steer-by-wire and the 298kW Red Sport twin-turbo V6.",
                "generations": [
                    {"series_code": "V37", "generation_name": "Q50", "years": {"start": 2014, "end": 2020}, "body_styles": ["Sedan"], "summary": "2.0L Turbo, 2.2L diesel, 3.5L Hybrid (268kW), and 3.0L Twin-Turbo V6 Red Sport 400 (298kW)."}
                ]
            },
            {
                "model_slug": "q60",
                "name": "Q60",
                "vehicle_type": "Coupe",
                "segment": "Sports Luxury Coupe",
                "years_sold_au": {"start": 2013, "end": 2020},
                "locally_built": False,
                "overview": "Sculpted luxury sports coupe offering 298kW twin-turbo V6 performance and active dynamic suspension.",
                "generations": [
                    {"series_code": "CV36/CV37", "generation_name": "Q60", "years": {"start": 2013, "end": 2020}, "body_styles": ["Coupe", "Convertible"], "summary": "3.7L V6 (CV36), then stunning CV37 with 2.0L Turbo and 298kW VR30DDTT V6 (Red Sport)."}
                ]
            },
            {
                "model_slug": "qx70",
                "name": "QX70 / FX",
                "vehicle_type": "SUV",
                "segment": "Large Luxury SUV",
                "years_sold_au": {"start": 2012, "end": 2020},
                "locally_built": False,
                "overview": "Bionic cheetah-styled sports crossover built on the FM rear-wheel-drive platform with available V8 power.",
                "generations": [
                    {"series_code": "S51", "generation_name": "FX / QX70", "years": {"start": 2012, "end": 2020}, "body_styles": ["5-door SUV"], "summary": "FX37 (3.7L V6), FX30d (3.0L V6 diesel), and FX50 (5.0L VK50VE V8 287kW); rebadged QX70 in 2014."}
                ]
            }
        ]
    },
    {
        "make_slug": "eunos",
        "name": "Eunos",
        "country_of_origin": "Japan",
        "years_active_au": {"start": 1992, "end": 1996},
        "currently_sold_au": False,
        "local_manufacturer": False,
        "overview": "Mazda's luxury channel in Australia, showcasing boutique dealerships, the world's smallest production V6, and the revolutionary Miller-cycle engine.",
        "australian_history": """In 1992, at the peak of Japan's automotive technology boom, Mazda Australia launched Eunos as a dedicated luxury channel to rival Lexus and prestige European brands. Eunos operated via standalone, boutique dealerships featuring personalized concierge customer service.

The brand debuted with three engineering marvels: the Eunos 30X sports coupe, powered by the world's smallest production V6 (the 1.8L K8-ZE 24-valve quad-cam engine); the Eunos 500 compact luxury sedan, featuring a 2.0L KF-ZE V6, Giorgio Giugiaro-praised bodywork, and a flawless multi-layer paint process; and the Eunos 800 flagship sedan in 1993. The Eunos 800 was celebrated globally for debuting the world's first production Miller-cycle automotive engine (the 2.3L KJ-ZEM with a Lysholm supercharger), generating the torque and power of a 3.0L V6 with the fuel economy of a 2.0L 4-cylinder.

Following the burst of Japan's bubble economy and currency shifts, Mazda consolidated its operations worldwide. In 1996, Mazda Australia dissolved the standalone Eunos channel. The Eunos 800 was integrated into the core Mazda lineup as the Mazda Eunos 800 and later renamed the Mazda Millenia until 2002.""",
        "models_catalog": [
            {
                "model_slug": "eunos-30x",
                "name": "Eunos 30X",
                "vehicle_type": "Coupe",
                "segment": "Sports Coupe",
                "years_sold_au": {"start": 1992, "end": 1996},
                "locally_built": False,
                "overview": "Aerodynamic liftback coupe powered by the world's smallest production 1.8L quad-cam V6 engine.",
                "generations": [
                    {"series_code": "EC", "generation_name": "Eunos 30X", "years": {"start": 1992, "end": 1996}, "body_styles": ["Coupe"], "summary": "1.8L K8-ZE V6 98kW revving to 7,800 rpm, front-wheel drive, 5-speed manual or 4-speed auto."}
                ]
            },
            {
                "model_slug": "eunos-500",
                "name": "Eunos 500",
                "vehicle_type": "Sedan",
                "segment": "Mid-size Luxury Sedan",
                "years_sold_au": {"start": 1992, "end": 1996},
                "locally_built": False,
                "overview": "Compact executive sedan renowned for stunning styling and silky 2.0L V6 refinement.",
                "generations": [
                    {"series_code": "CA", "generation_name": "Eunos 500", "years": {"start": 1992, "end": 1996}, "body_styles": ["Sedan"], "summary": "2.0L KF-ZE quad-cam V6 110kW, leather interior, high-luster multi-coat paint finish."}
                ]
            },
            {
                "model_slug": "eunos-800",
                "name": "Eunos 800",
                "vehicle_type": "Sedan",
                "segment": "Large Luxury Sedan",
                "years_sold_au": {"start": 1993, "end": 1996},
                "locally_built": False,
                "overview": "Flagship luxury sedan that introduced the world-first production Miller-cycle supercharged V6 engine.",
                "generations": [
                    {"series_code": "TA", "generation_name": "Eunos 800 / Millenia", "years": {"start": 1993, "end": 1996}, "body_styles": ["Sedan"], "summary": "2.3L Miller-cycle supercharged KJ-ZEM V6 (162kW) and 2.5L KL-DE V6; later sold as Mazda Millenia."}
                ]
            }
        ]
    }
]

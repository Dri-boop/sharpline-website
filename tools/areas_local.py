# Local text for each suburb page (shown under the photos), plus two suburb-specific FAQs.
# Rules: general local knowledge only, no invented jobs. Jobs may only be named where
# real_photos in areas_data.py confirm them.

LOCAL = {
  "maitland": dict(
    text="Maitland grew up along Voortrekker Road and the railway line, so many homes are older semis and freestanding houses from the early 1900s onwards, built close to the street. Original timber floors and doors often survive under later layers of paint and carpet. Behind the main road there is light industry and plenty of small businesses, which is why we fit counters, shelving and office partitions here as often as kitchens. Our workshop is in the 7th Avenue Business Park, so for Maitland jobs we can measure, build and fit with very little travel.",
    faqs=[("Can you fit out a small shop or office in Maitland?", "Yes. Counters, shelving, storage and partitions are built in our Maitland workshop and fitted after hours if that suits your business better."),
          ("Can old timber floors in a Maitland house be saved?", "Often, yes. We lift a few boards to check the joists and subfloor, replace what is rotten and match new boards to the old ones before sanding.")]),
  "woodstock": dict(
    text="Lower Woodstock is one of the oldest parts of Cape Town, with rows of Victorian semis and terraces, many with pressed ceilings, timber sash windows and narrow, deep plots. Upper Woodstock climbs the slope of Devil's Peak and has more freestanding houses with views over the harbour. Old warehouses along Albert Road have become studios, lofts and offices. In the older houses walls are rarely straight, so cupboards and kitchens have to be scribed to fit, and original joinery is usually worth repairing rather than replacing.",
    faqs=[("Can you match a new sash window to the old ones in my Woodstock house?", "Yes. We copy the profiles of the existing frames and glazing bars so the new window sits naturally next to the originals."),
          ("Do you do fit-outs in Woodstock's converted warehouses?", "Yes. Open-plan lofts and studios suit built-in storage, kitchen walls and partitions, and we plan around building access and lifts.")]),
  "salt-river": dict(
    text="Salt River sits between Woodstock and Observatory and grew around the railway workshops and factories, so its streets are lined with small workers' cottages and semis on tiny plots. Rooms are compact and ceilings are lower than in the grander Victorian suburbs nearby. Many homes are now rented out or used as live-work spaces, and some old factory buildings have become offices. Here the best results come from built-ins made to measure: a cupboard that fills an alcove to the ceiling, or a kitchen planned to the centimetre.",
    faqs=[("How do you fit a kitchen into a small Salt River cottage?", "We measure every wall and opening, then plan tall units, corner storage and slim appliances so nothing is wasted. Everything is built in our workshop and fitted in a day or two."),
          ("Can you make cupboards that stand up to tenants?", "Yes. For rentals we use hard-wearing board, solid hinges and runners, and finishes that are easy to clean and repair.")]),
  "observatory": dict(
    text="Observatory, or Obs, has some of Cape Town's best-kept Victorian cottages and semis, many with front stoeps, timber floors and decorative fretwork. It lies close to UCT and Groote Schuur Hospital, so a lot of houses are shared by students or young professionals. Parts of Obs near the Liesbeek River are low-lying and can be damp in winter, which matters for floors, skirting and anything built against outside walls. Owners usually want to keep the character, while landlords want finishes that last through several tenants.",
    faqs=[("My Obs house has damp walls. Can you still fit built-in cupboards?", "Yes, but we treat the cause first where possible, leave a ventilation gap behind the units and use moisture-resistant board near outside walls."),
          ("Can you restore the timber stoep or fretwork on a Victorian cottage?", "Yes. We repair or remake damaged timber to match the original pattern and seal it for the weather.")]),
  "mowbray": dict(
    text="Mowbray grew up around the old Main Road and the railway station, so many homes are older cottages and semis with suspended timber floors on joists. After decades of wear and damp, those boards and the timber below them can rot, which is the job our Mowbray photos show: rotten old boards lifted, then a new timber floor laid with fresh skirting. Being close to UCT, Mowbray also has many flats and student houses, where compact kitchens, study units and tough wardrobes are the usual requests.",
    faqs=[("How do you know if a timber floor needs replacing?", "Soft or bouncy boards, gaps and a musty smell are warning signs. We lift a few boards, check the joists and subfloor, and tell you honestly whether a repair or a new floor makes more sense."),
          ("Can you replace a floor without redoing the whole room?", "Yes. We can replace one room at a time, and fit new skirting so the finish looks complete.")]),
  "rosebank": dict(
    text="Rosebank lies between Mowbray and Rondebosch, below UCT's main campus and around the Baxter Theatre. Its streets have Victorian and Edwardian houses with high ceilings, big sash windows and fireplaces, many split into flats or rented to students. The tall walls and chimney breasts leave alcoves that suit built-in shelving and cupboards, and high ceilings mean wardrobes can go much taller than standard. Older kitchens here were often added on later, so refits sometimes start with fixing uneven floors and walls.",
    faqs=[("Can you build shelves into the alcoves next to a fireplace?", "Yes. Alcove shelving and cupboards are one of the most common jobs in older homes. We scribe them to the walls so there are no gaps."),
          ("How tall can a wardrobe be in a house with high ceilings?", "As tall as the room allows. We build them in sections so they fit through doors and stairs, then join them in place.")]),
  "pinelands": dict(
    text="Pinelands was South Africa's first garden city, laid out from 1919 with winding, tree-lined streets, big gardens and green belts. The oldest houses include thatched cottages, and most homes date from the 1940s to the 1970s, with generous plots and many pools. Original pine and hardwood floors are common under old carpets, and our Pinelands photo shows one brought back: a pine floor sanded and sealed. Kitchens and built-ins from that era are now often due for replacement with more practical modern layouts.",
    faqs=[("Can you sand and seal an old pine floor in Pinelands?", "Yes. We sand back to clean timber, fill gaps where needed and seal it. Pine is softer than hardwood, so we choose a finish that protects it."),
          ("Can you redo a 1960s kitchen without moving the plumbing?", "Usually, yes. Keeping the sink and stove positions saves cost, and a new layout of cupboards can still make the kitchen work much better.")]),
  "thornton": dict(
    text="Thornton is a small, quiet suburb between Pinelands and Epping, with freestanding family homes on decent plots, garages and established gardens. Many houses date from the middle of the last century and have been extended over the years, so floor levels, ceiling heights and window styles can change from room to room. Common work here is replacing original kitchens and wardrobes, upgrading front and garage doors, and building storage into extensions so they feel part of the house.",
    faqs=[("Can new cupboards in an extension match the rest of the house?", "Yes. We match door styles, colours and handles so the new room looks like it was always there."),
          ("Do you replace old garage doors in Thornton?", "Yes. We supply and fit new garage doors, including aluminium and glass options, and can fit them to existing openings.")]),
  "kensington": dict(
    text="Kensington, next to Maitland and Factreton, is an established working-class suburb of family homes, many built small and extended over the decades as families grew. Plots are modest, so additions often go to the back or up, and storage is always short. Typical work is a new kitchen in place of a tired original, built-in wardrobes in bedrooms, and solid front doors and security gates. We are a few minutes away in Maitland, which keeps site visits quick.",
    faqs=[("Can you build wardrobes in small bedrooms?", "Yes. Sliding doors save floor space, and taking the wardrobe up to the ceiling adds a lot of storage without taking more room."),
          ("Do you fit security gates and front doors?", "Yes. We fit solid timber and steel front doors and security gates, measured to your openings.")]),
  "brooklyn": dict(
    text="Brooklyn sits between Rugby, Ysterplaat and Milnerton, close to the N1 and Koeberg Road. Homes here are mostly older, smaller houses on compact plots, many with additions and backyard rooms. With limited space, good storage matters: our Brooklyn photo shows a compact kitchen with a tall pantry unit that uses the full height of the wall. Solid front doors, security gates and garage doors are other common upgrades in the area.",
    faqs=[("How do you get more storage into a small kitchen?", "Tall pantry units, drawers instead of doors in the base units and cupboards up to the ceiling all add space without making the room feel smaller."),
          ("Can you fit a kitchen around old, uneven walls?", "Yes. We measure carefully and scribe end panels and tops to the walls so the finish looks straight.")]),
  "cape-town-city-centre": dict(
    text="The city centre is mostly apartment blocks, converted office buildings, shops and offices, from old buildings on Long and Bree Streets to new towers on the Foreshore. Nearly everything is sectional title, so work needs the managing agent's or body corporate's approval, booked lifts and loading bays, and set working hours. Apartments are often small, so built-in storage, compact kitchens and fold-away desks make a real difference. We build in our workshop and bring pieces in ready to fit, which keeps time in the building short.",
    faqs=[("Do I need body corporate approval for a new kitchen in my CBD flat?", "Usually yes, especially if plumbing or electrical work changes. We can give you the drawings and timeline they ask for, and work within the building's hours."),
          ("How do you get large cupboards into an apartment building?", "We build them in sections sized for the lift and doors, then assemble and fix them in the apartment.")]),
  "gardens": dict(
    text="Gardens takes its name from the Company's Garden and runs up from the city towards Kloof Nek. It has Victorian and Edwardian houses with high ceilings, timber floors and sash windows, often right next to apartment blocks and townhouses. Around Kloof Street many homes are flats or rentals. In the older houses, original doors, floors and windows are worth saving, while in the flats the aim is to make every centimetre of storage count.",
    faqs=[("Can you restore original timber doors in a Gardens house?", "Yes. We repair damaged panels and frames, refit hinges and locks, and strip or repaint as needed."),
          ("Can you fit a wardrobe wall in a small apartment?", "Yes. A wall of sliding-door wardrobes up to the ceiling gives the most storage for the floor space it takes.")]),
  "tamboerskloof": dict(
    text="Tamboerskloof climbs the slopes below Lion's Head and Kloof Nek, with steep streets of Victorian houses, many with stoeps, balconies and terraces looking over the city. Plots are small and often terraced into the hill, so decks and outdoor living spaces are a big part of many homes. Plenty of houses are let as short-term rentals, which need tough, easy-to-clean finishes and fast turnarounds. Access on steep, narrow streets is part of planning any job here.",
    faqs=[("Can you build a deck on a sloping plot in Tamboerskloof?", "Yes. We set the frame level on posts or brackets to follow the slope, and use hardwood and stainless fixings that last outdoors."),
          ("Can you refit a short-let flat quickly between bookings?", "Yes. We build everything in the workshop first, so most refits take only a few days on site.")]),
  "oranjezicht": dict(
    text="Oranjezicht sits high on the slopes of Table Mountain above the city, around De Waal Park. Homes are mostly larger family houses, many with pools, terraces and views over the City Bowl, alongside some older character homes and apartment blocks. The upper streets catch strong south-easter winds in summer, so outdoor timber, gates and doors need sturdy fixings. Kitchens and living areas here are often opened up to terraces, so indoor and outdoor finishes have to work together.",
    faqs=[("What timber lasts for a deck that faces the south-easter?", "A dense hardwood with stainless steel screws and a good sealer. We fix boards so they can move without lifting."),
          ("Can you match a new kitchen to an older Oranjezicht home?", "Yes. We can do shaker-style or classic doors that suit an older house, with modern hardware inside.")]),
  "vredehoek": dict(
    text="Vredehoek lies on the slopes of Devil's Peak above the city, along De Waal Drive. It mixes apartment blocks with family homes, and it is one of the windiest parts of the City Bowl when the south-easter blows. That wind tests doors, windows, gates and anything built outside, so hinges, seals and fixings need to be solid. In the apartments, compact kitchens and built-in storage are the usual requests.",
    faqs=[("Can you make doors that don't rattle in the south-easter?", "Yes. Well-fitted frames, good seals and quality hinges and locks stop most rattling and draughts."),
          ("Do you do kitchens in Vredehoek apartments?", "Yes. We measure the space, build in our workshop and install with minimum time in the building.")]),
  "bo-kaap": dict(
    text="The Bo-Kaap, on the slopes of Signal Hill above the city, is one of Cape Town's oldest neighbourhoods, known for its brightly painted cottages and cobbled streets. Much of it is a heritage protection area, so changes to street-facing walls, doors and windows can need heritage approval. The cottages are small and often very old, with thick walls and uneven floors. Timber doors, windows and frontages need careful repair or exact copies, while inside the aim is good storage in small rooms.",
    faqs=[("Do I need approval to replace a front door in the Bo-Kaap?", "Often, yes, because much of the area is a heritage protection area. We can make a door that copies the original style and give you drawings for the application."),
          ("Can you fit modern cupboards in an old Bo-Kaap cottage?", "Yes. We scribe them to thick, uneven walls so they fit neatly without changing the character of the house.")]),
  "de-waterkant": dict(
    text="De Waterkant sits between the city and Green Point, with cobbled streets, small restored cottages and modern apartment blocks. Many homes are short-let rentals or second homes, so owners want refits that are quick, tidy and look good in photos. Space is tight in the cottages, and in the apartment blocks work has to fit body corporate rules and building hours. Clean, simple kitchens and built-in storage are the usual requests.",
    faqs=[("Can you refit a short-let apartment in De Waterkant quickly?", "Yes. Everything is made in our workshop, so time on site is short and the flat is back on the market sooner."),
          ("Do you work within body corporate rules?", "Yes. We plan deliveries, noise and working hours around what the building allows.")]),
  "green-point": dict(
    text="Green Point stretches from the stadium and Green Point Park to the Sea Point border, with apartment blocks, townhouses and some older homes. Being so close to the sea, salt air quickly attacks ordinary hinges, handles and screws, so we use stainless or coated hardware where it matters. Many flats are rentals or holiday lets. Our Green Point photos show a kitchen with an island and timber shelving, and a kitchen breakfast bar.",
    faqs=[("What hardware lasts near the sea in Green Point?", "Stainless steel or properly coated hinges, handles and screws. Standard hardware can rust within a year or two this close to the sea."),
          ("Can you add an island or breakfast bar to an apartment kitchen?", "Often, yes, if there is space to walk around it. We plan it with you so it adds storage and seating without crowding the room.")]),
  "sea-point": dict(
    text="Sea Point runs along the Atlantic coast below Signal Hill and Lion's Head, with its promenade and long rows of apartment blocks, from 1930s art deco buildings to modern towers. Most homes are sectional-title flats, so renovations need body corporate approval and must respect building hours and lift bookings. Kitchens and storage are often small, and the sea air is hard on hardware. Built-in wardrobes and compact kitchens are the jobs we are most often asked about here.",
    faqs=[("Will my Sea Point body corporate allow a kitchen renovation?", "Most do, with approval first. We provide the plan, timeline and working hours they usually ask for."),
          ("Can you keep an art deco feel in a new kitchen?", "Yes. Simple lines, curved details and the right handles can suit an older building while using modern materials.")]),
  "fresnaye": dict(
    text="Fresnaye sits on the slopes between Sea Point and Lion's Head, with mostly large homes on steep plots, many with pools, terraces and big windows facing the sea. Homes here are often built for entertaining, with large kitchens, sculleries and bars. The combination of sun, salt air and wind is hard on outdoor timber and hardware, so materials need to be chosen with care and maintained.",
    faqs=[("Can you build a scullery behind a main kitchen?", "Yes. A scullery keeps dishes and appliances out of sight. We design both together so the finishes match."),
          ("How often does a pool deck in Fresnaye need sealing?", "Usually once or twice a year, depending on sun exposure. We'll show you how to keep it in good condition.")]),
  "bantry-bay": dict(
    text="Bantry Bay is a small, steep pocket between Sea Point and Clifton, on the lower slopes of Lion's Head, and fairly sheltered from the south-easter. Homes are mostly apartment blocks and large modern houses facing the sea, many with concrete walls, big glass doors and curved shapes. In a modern home like this, flooring has to follow the architecture: our Bantry Bay photos show an oak herringbone floor being laid and then finished, cut in neatly around a curved wall.",
    faqs=[("Can herringbone flooring follow a curved wall?", "Yes. Each block at the edge is cut to the curve, so the pattern runs right up to the wall with no gaps."),
          ("Is oak a good floor for a home near the sea?", "Indoors, yes. Oak is hard-wearing, and with a good finish it handles sand and daily use well.")]),
  "camps-bay": dict(
    text="Camps Bay lies below the Twelve Apostles, facing the Atlantic, and its homes are built for outdoor living: pools, roof terraces, decks and big sliding doors. Strong sun, salt air and wind mean outdoor timber has to be dense hardwood fixed with stainless steel, and sealed regularly. Our Camps Bay photos show a hardwood roof deck with sea views and steps up to a hot tub. Holiday homes and rentals here also need hard-wearing kitchens and finishes.",
    faqs=[("Can you build a deck on a flat roof in Camps Bay?", "Yes. We build a frame that sits on the roof without damaging the waterproofing, then lay hardwood boards on top."),
          ("Can you build steps or a surround for a hot tub?", "Yes. We build hardwood steps and surrounds to fit the tub, with access panels for the pump.")]),
  "rondebosch": dict(
    text="Rondebosch is one of Cape Town's oldest suburbs, home to UCT, Rondebosch Common and several well-known schools. It has large family homes, older character houses with timber floors, and many student houses. Our Rondebosch photos show an attic converted into an office, from new ceiling joists and floor framing to a finished plywood floor and panelled walls, as well as an old timber floor opened up for repair and a hardwood pool deck being built.",
    faqs=[("Can you turn an attic into a usable room?", "Often, yes. We check the roof structure, add joists and a proper floor, then line the walls. In Rondebosch we've converted an attic into an office."),
          ("Can you repair just part of an old timber floor?", "Yes. We open up the damaged section, fix the joists and subfloor, and fit matching boards.")]),
  "newlands": dict(
    text="Newlands sits on the eastern slopes of Table Mountain, next to the forest and the sports grounds, and it is one of the wettest parts of Cape Town. Its leafy streets have family homes with big gardens, many shaded by old trees. The wet winters mean damp is a real concern: kitchen and bathroom cupboards, floors and outdoor timber need moisture-resistant materials and good ventilation. Decks under trees also need regular cleaning and sealing.",
    faqs=[("What cupboards work best in a damp Newlands home?", "Moisture-resistant board, sealed edges and a small gap behind units against outside walls help a lot."),
          ("Will a timber deck rot under the trees in Newlands?", "Not if it's built right. Hardwood, good drainage and regular sealing keep it sound for many years.")]),
  "claremont": dict(
    text="Claremont is a busy Southern Suburbs centre around Cavendish Square, with family homes on its quieter streets, many townhouse complexes and apartment blocks. Homes in complexes often come with rules about outside changes and working hours. Upper Claremont has larger houses on bigger plots. Common work here is modern kitchens, built-in wardrobes and storage for townhouses where space is planned tightly.",
    faqs=[("Can you work in a Claremont townhouse complex?", "Yes. We follow the complex's rules on working hours, parking and deliveries."),
          ("Can you add storage under a staircase?", "Yes. Pull-out drawers or cupboards under stairs turn dead space into useful storage.")]),
  "kenilworth": dict(
    text="Kenilworth, home of the Kenilworth racecourse, has established family homes on leafy streets, along with townhouses and some apartment blocks. Many houses date from the early to mid 1900s and have been updated over time. Typical work here is replacing older kitchens, adding built-in wardrobes, and new garage and front doors. Close to the M3 and Main Road, it is an easy trip from our Maitland workshop.",
    faqs=[("Can you replace an old kitchen in a Kenilworth home?", "Yes. We remove the old units, check the walls and plumbing points, and fit a new kitchen built in our workshop."),
          ("Do you fit new garage doors?", "Yes, including aluminium and glass garage doors made to measure.")]),
  "wynberg": dict(
    text="Wynberg ranges from the Victorian cottages of Chelsea Village and the area around Maynardville to larger family homes on Wynberg Hill. The older cottages have timber floors, sash windows and pressed ceilings worth keeping, while the bigger homes often need full modern renovations. So in Wynberg we do both careful restoration and new kitchens, built-ins and doors.",
    faqs=[("Can you restore sash windows in a Chelsea Village cottage?", "Yes. We repair or remake frames and sashes to match the originals."),
          ("Can you modernise a kitchen in an old cottage without losing its character?", "Yes. Classic door styles and natural timber can sit well in an old house while giving you a modern layout.")]),
  "plumstead": dict(
    text="Plumstead has family homes on good-sized plots, with gardens, garages and room to extend. Renovations, extensions and outdoor living areas are common here. Kitchens are often opened up to living rooms, and families want built-in storage for bedrooms and garages. Decks and covered patios make the most of the garden.",
    faqs=[("Can you open up a kitchen to the living room?", "We do the carpentry and fitting, and work with trusted builders and electricians for wall and wiring changes."),
          ("Can you build storage in a garage?", "Yes. Shelving and cupboards along the walls keep tools and sports gear off the floor.")]),
  "constantia": dict(
    text="Constantia is known for its wine farms, oak-lined roads and large homes on big plots, many with pools, entertainment areas and generous kitchens. Greenbelts and mature trees give it a country feel. Homes here often want high-end kitchens with sculleries, walk-in wardrobes and dressing rooms, solid timber front doors and outdoor timber around pools.",
    faqs=[("Do you build walk-in wardrobes and dressing rooms?", "Yes. We design the layout around how you use the space, with hanging, drawers and shoe storage."),
          ("Can you make a solid timber front door?", "Yes. We make front doors to size, in a style that suits the house.")]),
  "athlone": dict(
    text="Athlone is an established Cape Flats suburb of family homes, many extended over the years as families grew, with additions at the back or upstairs. Plots are modest and households are often large, so storage and a practical kitchen matter. Our Athlone photo shows a white scullery with grey tops. Built-in wardrobes, solid doors and security gates are other common upgrades here.",
    faqs=[("Can you build a scullery next to a kitchen?", "Yes. In Athlone we've built a white scullery with grey tops. A scullery keeps washing up and appliances out of the main kitchen."),
          ("Can you fit cupboards in an extension?", "Yes. We measure once the walls are up and build cupboards to fit the new room exactly.")]),
  "goodwood": dict(
    text="Goodwood runs along Voortrekker Road near the showgrounds, with family homes and semi-detached houses, many from the early and middle 1900s. Lots of young families are buying and renovating here, so kitchens, bathrooms and bedrooms are being modernised. Many homes also need new front doors, gates and garage doors. It is only a short drive from our Maitland workshop.",
    faqs=[("Can you renovate a kitchen in an older Goodwood semi?", "Yes. We plan the new layout around the existing space and build everything in our workshop."),
          ("Do you fit front doors and gates in Goodwood?", "Yes. We measure, supply and fit doors and gates to your openings.")]),
  "parow": dict(
    text="Parow sits on Voortrekker Road between Goodwood and Bellville, near Tygerberg Hospital, with family homes, semis and apartment blocks. Many homes are older and being renovated, while flats need compact kitchens and good storage. Kitchen and bedroom upgrades, TV units and doors are common jobs here.",
    faqs=[("Can you build a TV unit with storage?", "Yes. We design TV units with drawers, shelves and hidden cable routes to fit your wall."),
          ("Do you do kitchens in Parow flats?", "Yes. We plan compact kitchens to make the most of small spaces.")]),
  "bellville": dict(
    text="Bellville is a major Northern Suburbs centre, with a busy business district, Tyger Valley, and family homes and apartments on its quieter streets. The University of the Western Cape and Stellenbosch University's Tygerberg campus are nearby, so there are many rentals. We do home renovations here, as well as counters, offices and shop fittings for businesses.",
    faqs=[("Do you fit out offices and shops in Bellville?", "Yes. Counters, reception desks, storage and partitions are built in our workshop and fitted on site."),
          ("Can you build durable cupboards for a rental?", "Yes. We use hard-wearing board, solid hinges and finishes that are easy to clean.")]),
  "durbanville": dict(
    text="Durbanville sits at the edge of the Northern Suburbs, near the Durbanville wine valley, with newer family homes and security estates, many with pools, double garages and entertainment areas. Summers are hot and dry, so outdoor timber needs protection from the sun. Estates often have design rules for outside changes. Family kitchens, built-in cupboards, garage doors and pool decks are common requests.",
    faqs=[("Do estate rules affect a new garage door or deck?", "Often, yes. We can give you drawings and details to get estate approval before we start."),
          ("How do you protect a deck from Durbanville's summer sun?", "We use hardwood and a UV-resistant sealer, and recommend resealing regularly.")]),
  "milnerton": dict(
    text="Milnerton lies along the lagoon and the coast north of the city, with family homes, townhouses and apartments, including Woodbridge Island and the areas around Rietvlei. Being close to the sea, salt air and wind affect hardware and outdoor timber. Common work here is kitchens, built-in cupboards, decks and doors with hardware that resists rust.",
    faqs=[("What decking lasts near the Milnerton lagoon?", "Dense hardwood with stainless fixings, sealed regularly against sun and salt."),
          ("Can you fit kitchens in Milnerton townhouses?", "Yes. We follow complex rules on access and working hours.")]),
  "century-city": dict(
    text="Century City is a modern mixed-use area built around canals and Canal Walk, with apartment blocks, offices and hotels. Homes are mostly modern apartments, often compact, managed by property associations with rules on deliveries and working hours. Clever storage, sleek kitchens and home-office units are what people ask for most here.",
    faqs=[("Can you fit a home office in a Century City apartment?", "Yes. A built-in desk with shelving and cupboards can fit into a corner or alcove."),
          ("Do you follow property association rules?", "Yes. We plan deliveries, access and working hours around the building's rules.")]),
  "table-view": dict(
    text="Table View faces Table Mountain across the bay, with family homes close to the beach and plenty of townhouse complexes. It is known for strong summer wind, which brings sand and salt into everything. Doors, windows, garage doors and outdoor timber here need sturdy, rust-resistant hardware and regular care. Kitchens and built-in cupboards are the most common indoor upgrades.",
    faqs=[("How do I keep sand and wind out around my doors?", "Well-fitted frames, good seals and solid hardware make a big difference in Table View's wind."),
          ("Will a timber garage door survive near the beach?", "With the right timber, finish and stainless hardware, yes, but it needs regular maintenance. Aluminium is a low-maintenance option.")]),
  "khayelitsha": dict(
    text="Khayelitsha is one of Cape Town's largest townships, with family homes of every size, from small starter houses to large homes extended over the years. Storage is often short as families grow, so well-planned built-in cupboards make a big difference. Our Khayelitsha photos show sliding wardrobes with open shelving, a shelf tower, and the shelves and rails inside.",
    faqs=[("Can you build sliding wardrobes in small bedrooms?", "Yes. In Khayelitsha we've built sliding-door wardrobes with shelves and rails. Sliding doors save space because they don't swing open."),
          ("Can you build cupboards in an extended room?", "Yes. We measure the new room and build cupboards to fit it exactly.")]),
  "langa": dict(
    text="Langa, founded in the 1920s, is Cape Town's oldest township, just beside Pinelands and only minutes from our Maitland workshop. Homes are compact, and many have backyard units and extensions. A well-planned kitchenette, built-in cupboards and a tidy bathroom vanity make the most of small spaces. Our Langa photo shows finishing touches and the clean-up after a job.",
    faqs=[("Can you fit a kitchenette in a backyard unit?", "Yes. We plan compact kitchenettes with storage, a sink and space for appliances."),
          ("Do you clean up after the job?", "Yes. We remove offcuts, dust and packaging and leave the space clean.")]),
  "blue-downs": dict(
    text="Blue Downs, near Eerste River and Kuils River, has family homes, many built from the 1980s onwards and extended since. Kitchens, built-in cupboards and TV units are the most popular upgrades. Our Blue Downs photos show a white gloss kitchen with granite tops being installed and finished.",
    faqs=[("Can you fit a gloss kitchen with granite tops?", "Yes. In Blue Downs we've installed a white gloss kitchen with granite tops. We build the units and coordinate the stone tops."),
          ("Do you build TV units?", "Yes. We design TV units with storage to fit your wall and your equipment.")]),
  "lansdowne": dict(
    text="Lansdowne, on the Cape Flats side of the Southern Suburbs, has established family homes and blocks of flats. Kitchens are often small, so compact layouts and good storage are in demand. Our Lansdowne photo shows a white kitchenette with pendant lights. Built-in wardrobes and solid doors are other common upgrades here.",
    faqs=[("Can you fit a kitchenette in a small flat?", "Yes. In Lansdowne we've fitted a white kitchenette. We plan every centimetre for storage and workspace."),
          ("Can you build wardrobes in a flat?", "Yes. Built-in wardrobes up to the ceiling give the most storage in small rooms.")]),
  "bloubergstrand": dict(
    text="Blouberg, with Big Bay and the classic view of Table Mountain across the water, has family homes and townhouses close to the beach. Wind, sand and salt air are part of life here, so hardware and finishes need to be chosen with care. Our Blouberg photos show a white kitchen with a teal splashback and a laundry nook being installed and finished.",
    faqs=[("Can you include a laundry space in a kitchen?", "Yes. In Blouberg we've built a kitchen with a laundry nook. A tall cupboard or recess can hide the washing machine."),
          ("What finishes last near the beach in Blouberg?", "Moisture-resistant board, quality wrapped or sprayed doors, and stainless or coated hardware.")]),
  "devils-peak": dict(
    text="Devil's Peak Estate sits on the slopes of Devil's Peak above the city, with homes and apartments enjoying views over the harbour and City Bowl. Many have roof terraces and decks that face strong sun and the south-easter. Our Devil's Peak photos show a hardwood roof deck with city views, and measuring up for an office fit-out.",
    faqs=[("Can you build a roof deck with city views?", "Yes. In Devil's Peak we've built a hardwood roof deck, framed to protect the roof and fixed with stainless steel."),
          ("Do you do office fit-outs?", "Yes. We measure, design and build desks, storage and partitions for offices.")]),
  "kuils-river": dict(
    text="Kuils River lies on the eastern side of the Northern Suburbs, near the Stellenbosch wine country, with family homes and newer developments. Many families are upgrading kitchens, adding built-in cupboards and fitting garage doors. Summers are hot, so outdoor timber needs protection from the sun.",
    faqs=[("Do you fit kitchens on new developments?", "Yes. We can fit kitchens in new homes once the walls and plumbing are ready."),
          ("Can you replace garage doors in Kuils River?", "Yes. We supply and fit garage doors to existing openings.")]),
  "epping": dict(
    text="Epping is mostly industrial and commercial, with Epping Industria and the Epping Market, so our work here is for businesses. Counters, reception desks, offices, storage and shop fittings need to stand up to daily use. Being about 10 minutes from our Maitland workshop, deliveries and fitting are quick.",
    faqs=[("Can you build a reception desk for my business?", "Yes. We design and build reception desks and counters to suit your space and brand."),
          ("Can you install outside business hours?", "Yes, if that suits you better. We plan installs to avoid disrupting your work.")]),
  "plattekloof": dict(
    text="Plattekloof sits on the hills of the Northern Suburbs with wide views over the city and Table Mountain. Homes are mostly larger family houses, many with pools, entertainment areas and big kitchens. Hillside plots can be windy, so decks and outdoor timber need solid fixing.",
    faqs=[("Can you build a pool deck on a sloping plot?", "Yes. We build a level frame on posts to suit the slope, using hardwood and stainless fixings."),
          ("Do you build large family kitchens?", "Yes. We design kitchens with islands, sculleries and plenty of storage.")]),
  "durban": dict(
    text="Durban has a humid, subtropical climate, very different from Cape Town's, and timber moves more in humidity. That affects how furniture and joinery should be built and finished. Our Durban photos show pine bookcases and a pine serving stand built for clients there. For projects outside the Western Cape, we agree measurements, materials and timelines upfront, build in our Maitland workshop and arrange delivery.",
    faqs=[("How do you deliver furniture to Durban?", "We build it in our Maitland workshop and arrange delivery. Larger pieces are made to come apart for transport."),
          ("Does Durban's humidity affect timber furniture?", "Yes. We allow for timber movement in the design and use finishes that seal the wood well.")]),
  "eastern-cape": dict(
    text="Projects in the Eastern Cape are planned carefully before we travel: scope, materials, timeline and accommodation are agreed upfront. Our Eastern Cape photos show a roof project at Southridge, with tiled and sheeted roofs. Roofing and structural carpentry need careful planning around the weather and delivery of materials.",
    faqs=[("Do you do roofing in the Eastern Cape?", "Yes. We've completed a roof project at Southridge in the Eastern Cape, with tiled and sheeted roofs."),
          ("How do you plan a project outside Cape Town?", "We agree the scope, materials and timeline in writing before travelling, so there are no surprises.")]),
}

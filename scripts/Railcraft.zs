import mods.nei.NEI;



#
#-------------Tracks-------------
#
recipes.remove(<Railcraft:track>);
recipes.addShaped(<Railcraft:track>.withTag({track: "railcraft:track.junction"}) * 16, 
	[[<Railcraft:part.rail>, <Railcraft:part.rail>, <Railcraft:part.rail>],
	[<Railcraft:part.rail>, <Railcraft:part.railbed>, <Railcraft:part.rail>],
	[<Railcraft:part.rail>, <Railcraft:part.rail>, <Railcraft:part.rail>]]);

recipes.addShaped(<Railcraft:track>.withTag({track: "railcraft:track.whistle"}) * 16, 
	[[<Railcraft:part.rail>, null, <Railcraft:part.rail>],
	[<Railcraft:part.rail>, <Railcraft:part.railbed>, <Railcraft:part.rail>],
	[<Railcraft:part.rail>, <Railcraft:tool.whistle.tuner>, <Railcraft:part.rail>]]);
	
recipes.addShaped(<Railcraft:track>.withTag({track: "railcraft:track.suspended"}) * 16, 
	[[<Railcraft:part.rail>, <Railcraft:part.tie>, <Railcraft:part.rail>],
	[<Railcraft:part.rail>, <Railcraft:part.tie>, <Railcraft:part.rail>],
	[<Railcraft:part.rail>, <Railcraft:part.tie>, <Railcraft:part.rail>]]);
	
recipes.addShaped(<Railcraft:track>.withTag({track: "railcraft:track.embarking"}) * 16, 
	[[<Railcraft:part.rail:1>, <minecraft:ender_pearl>, <Railcraft:part.rail:1>], 
	[<Railcraft:part.rail:1>, <Railcraft:part.railbed>, <Railcraft:part.rail:1>], 
	[<Railcraft:part.rail:1>, <minecraft:ender_pearl>, <Railcraft:part.rail:1>]]);

recipes.addShaped(<Railcraft:track>.withTag({track: "railcraft:track.gated.oneway"}) * 8, 
	[[<Railcraft:part.rail>, <minecraft:fence_gate:*>, <Railcraft:part.rail>], 
	[<Railcraft:part.rail:1>, <Railcraft:part.railbed>, <Railcraft:part.rail:1>], 
	[<Railcraft:part.rail>, <minecraft:fence_gate:*>, <Railcraft:part.rail>]]);

recipes.addShaped(<Railcraft:track>.withTag({track: "railcraft:track.speed.wye"}) * 16, 
	[[<Railcraft:part.rail:3>, <Railcraft:part.rail:3>, <Railcraft:part.rail:3>], 
	[<Railcraft:part.rail:3>, <Railcraft:part.rail:3>, <Railcraft:part.railbed:1>], 
	[<Railcraft:part.rail:3>, <Railcraft:part.rail:3>, <Railcraft:part.rail:3>]]);
	
recipes.addShaped(<Railcraft:track>.withTag({track: "railcraft:track.slow.junction"}) * 16, 
	[[<Railcraft:part.rail:2>, <Railcraft:part.rail:2>, <Railcraft:part.rail:2>], 
	[<Railcraft:part.rail:2>, <Railcraft:part.railbed>, <Railcraft:part.rail:2>], 
	[<Railcraft:part.rail:2>, <Railcraft:part.rail:2>, <Railcraft:part.rail:2>]]);
	
recipes.addShaped(<Railcraft:track>.withTag({track: "railcraft:track.slow.wye"}) * 16, 
	[[<Railcraft:part.rail:2>, <Railcraft:part.rail:2>, <Railcraft:part.rail:2>], 
	[<Railcraft:part.rail:2>, <Railcraft:part.rail:2>, <Railcraft:part.railbed>], 
	[<Railcraft:part.rail:2>, <Railcraft:part.rail:2>, <Railcraft:part.rail:2>]]);
	
recipes.addShaped(<Railcraft:track>.withTag({track: "railcraft:track.electric"}) * 32, 
	[[<Railcraft:part.rail:5>, null, <Railcraft:part.rail:5>], 
	[<Railcraft:part.rail:5>, <Railcraft:part.railbed:1>, <Railcraft:part.rail:5>], 
	[<Railcraft:part.rail:5>, null, <Railcraft:part.rail:5>]]);
	
recipes.addShaped(<Railcraft:track>.withTag({track: "railcraft:track.electric.junction"}) * 16, 
	[[<Railcraft:part.rail:5>, <Railcraft:part.rail:5>, <Railcraft:part.rail:5>], 
	[<Railcraft:part.rail:5>, <Railcraft:part.railbed:1>, <Railcraft:part.rail:5>], 
	[<Railcraft:part.rail:5>, <Railcraft:part.rail:5>, <Railcraft:part.rail:5>]]);
	
recipes.addShaped(<Railcraft:track>.withTag({track: "railcraft:track.electric.wye"}) * 16, 
	[[<Railcraft:part.rail:5>, <Railcraft:part.rail:5>, <Railcraft:part.rail:5>], 
	[<Railcraft:part.rail:5>, <Railcraft:part.rail:5>, <Railcraft:part.railbed:1>], 
	[<Railcraft:part.rail:5>, <Railcraft:part.rail:5>, <Railcraft:part.rail:5>]]);
	
recipes.addShaped(<Railcraft:track>.withTag({track: "railcraft:track.coupler"}) * 16, 
	[[<Railcraft:part.rail:1>, <Railcraft:tool.crowbar>, <Railcraft:part.rail:1>], 
	[<Railcraft:part.rail:1>, <Railcraft:part.railbed>, <Railcraft:part.rail:1>], 
	[<Railcraft:part.rail:1>, <Railcraft:tool.crowbar>, <Railcraft:part.rail:1>]]);
	
recipes.addShaped(<Railcraft:track>.withTag({track: "railcraft:track.launcher"}) * 2, 
	[[<Railcraft:part.rail:4>, <Railcraft:part.railbed:1>, <Railcraft:part.rail:4>], 
	[<ore:blockSteel>, <minecraft:piston:*>, <ore:blockSteel>], 
	[<Railcraft:part.rail:4>, <Railcraft:part.railbed:1>, <Railcraft:part.rail:4>]]);
	
recipes.addShaped(<Railcraft:track>.withTag({track: "railcraft:track.control"}) * 32, 
	[[<Railcraft:part.rail>, <ore:dustRedstone>, <Railcraft:part.rail>], 
	[<Railcraft:part.rail:1>, <Railcraft:part.railbed>, <Railcraft:part.rail:1>], 
	[<Railcraft:part.rail>, <ore:dustRedstone>, <Railcraft:part.rail>]]);
	
recipes.addShaped(<Railcraft:track>.withTag({track: "railcraft:track.detector.direction"}) * 16, 
	[[<Railcraft:part.rail>, <ore:dustRedstone>, <Railcraft:part.rail>], 
	[<Railcraft:part.rail>, <Railcraft:part.railbed>, <Railcraft:part.rail>], 
	[<Railcraft:part.rail>, <minecraft:stone_pressure_plate:*>, <Railcraft:part.rail>]]);
	
recipes.addShaped(<Railcraft:track>.withTag({track: "railcraft:track.speed.boost"}) * 16, 
	[[<Railcraft:part.rail:3>, <ore:dustRedstone>, <Railcraft:part.rail:3>], 
	[<Railcraft:part.rail:3>, <Railcraft:part.railbed:1>, <Railcraft:part.rail:3>], 
	[<Railcraft:part.rail:3>, <ore:dustRedstone>, <Railcraft:part.rail:3>]]);
	
recipes.addShaped(<Railcraft:track>.withTag({track: "railcraft:track.slow.boost"}) * 16, 
	[[<Railcraft:part.rail:2>, null, <Railcraft:part.rail:2>], 
	[<minecraft:gold_ingot>, <Railcraft:part.railbed>, <minecraft:gold_ingot>], 
	[<Railcraft:part.rail:2>, <ore:dustRedstone>, <Railcraft:part.rail:2>]]);
	
recipes.addShaped(<Railcraft:track>.withTag({track: "railcraft:track.routing"}) * 16, 
	[[<Railcraft:part.rail>, <ore:dustRedstone>, <Railcraft:part.rail>], 
	[<Railcraft:part.rail>, <Railcraft:part.railbed>, <Railcraft:part.rail>], 
	[<Railcraft:part.rail>, <Railcraft:routing.ticket>, <Railcraft:part.rail>]]);
	
recipes.addShaped(<Railcraft:track>.withTag({track: "railcraft:track.routing"}) * 16, 
	[[<Railcraft:part.rail>, <ore:dustRedstone>, <Railcraft:part.rail>], 
	[<Railcraft:part.rail>, <Railcraft:part.railbed>, <Railcraft:part.rail>], 
	[<Railcraft:part.rail>, <Railcraft:routing.ticket.gold>, <Railcraft:part.rail>]]);
	
recipes.addShaped(<Railcraft:track:2264>.withTag({track: "railcraft:track.disposal"}) * 16, 
	[[<Railcraft:part.rail>, <Railcraft:part.tie>, <Railcraft:part.rail>], 
	[<Railcraft:part.rail>, <ore:blockSteel>, <Railcraft:part.rail>], 
	[<Railcraft:part.rail>, <Railcraft:part.tie>, <Railcraft:part.rail>]]);
	
recipes.remove(<Railcraft:track:2264>.withTag({track: "railcraft:track.disposal"}));
recipes.addShaped(<Railcraft:track:2264>.withTag({track: "railcraft:track.disposal"}) * 16, 
	[[<Railcraft:part.rail>, <Railcraft:part.tie>, <Railcraft:part.rail>], 
	[<Railcraft:part.rail>, <ore:blockSteel>, <Railcraft:part.rail>], 
	[<Railcraft:part.rail>, <Railcraft:part.tie>, <Railcraft:part.rail>]]);

recipes.remove(<Railcraft:track:8103>.withTag({track: "railcraft:track.priming"}));
recipes.addShaped(<Railcraft:track:8103>.withTag({track: "railcraft:track.priming"}), 
	[[<Railcraft:part.rail:4>, <minecraft:stone_pressure_plate:*>, <Railcraft:part.rail:4>], 
	[<Railcraft:part.rail:4>, <Railcraft:part.railbed:1>, <Railcraft:part.rail:4>], 
	[<Railcraft:part.rail:4>, <minecraft:flint_and_steel>, <Railcraft:part.rail:4>]]);

#	Reinforced

recipes.addShaped(<Railcraft:track>.withTag({track: "railcraft:track.reinforced"}) * 32, 
	[[<Railcraft:part.rail:4>, null, <Railcraft:part.rail:4>], 
	[<Railcraft:part.rail:4>, <Railcraft:part.railbed:1>, <Railcraft:part.rail:4>], 
	[<Railcraft:part.rail:4>, null, <Railcraft:part.rail:4>]]);
	
recipes.addShaped(<Railcraft:track>.withTag({track: "railcraft:track.reinforced.boost"}) * 16, 
	[[<Railcraft:part.rail:4>, null, <Railcraft:part.rail:4>], 
	[<Railcraft:part.rail:4>, <Railcraft:part.railbed:1>, <Railcraft:part.rail:4>], 
	[<Railcraft:part.rail:4>, <ore:dustRedstone>, <Railcraft:part.rail:4>]]);
	
recipes.addShaped(<Railcraft:track>.withTag({track: "railcraft:track.reinforced.switch"}) * 16, 
	[[<Railcraft:part.rail:4>, <Railcraft:part.railbed:1>, <Railcraft:part.rail:4>], 
	[<Railcraft:part.rail:4>, <Railcraft:part.rail:4>, <Railcraft:part.rail:4>], 
	[<Railcraft:part.rail:4>, <Railcraft:part.rail:4>, <Railcraft:part.rail:4>]]);
	
recipes.addShaped(<Railcraft:track>.withTag({track: "railcraft:track.reinforced.wye"}) * 16, 
	[[<Railcraft:part.rail:4>, <Railcraft:part.rail:4>, <Railcraft:part.rail:4>], 
	[<Railcraft:part.rail:4>, <Railcraft:part.rail:4>, <Railcraft:part.railbed:1>], 
	[<Railcraft:part.rail:4>, <Railcraft:part.rail:4>, <Railcraft:part.rail:4>]]);
	
recipes.addShaped(<Railcraft:track:764>.withTag({track: "railcraft:track.reinforced.junction"}) * 16, 
	[[<Railcraft:part.rail:4>, <Railcraft:part.rail:4>, <Railcraft:part.rail:4>], 
	[<Railcraft:part.rail:4>, <Railcraft:part.railbed:1>, <Railcraft:part.rail:4>], 
	[<Railcraft:part.rail:4>, <Railcraft:part.rail:4>, <Railcraft:part.rail:4>]]);





#
#-------------Components-------------
#

<ore:ingotSteel>.remove(<Railcraft:ingot>);
<ore:ingotCopper>.remove(<Railcraft:ingot:1>);
<ore:ingotTin>.remove(<Railcraft:ingot:2>);
<ore:ingotLead>.remove(<Railcraft:ingot:3>);
<ore:nuggetIron>.remove(<Railcraft:nugget>);
<ore:nuggetTin>.remove(<Railcraft:nugget:3>);
<ore:nuggetLead>.remove(<Railcraft:nugget:4>);

furnace.remove(<Railcraft:ingot:1>);
furnace.remove(<Railcraft:ingot:2>);
furnace.remove(<Railcraft:nugget:1>);
recipes.remove(<Railcraft:nugget>);
recipes.remove(<Railcraft:nugget:4>);
recipes.remove(<Railcraft:nugget:3>);
recipes.remove(<Railcraft:nugget:2>);
recipes.remove(<Railcraft:nugget:1>);
recipes.remove(<Railcraft:ingot>);
recipes.remove(<Railcraft:ingot:1>);
recipes.remove(<Railcraft:ingot:2>);
recipes.remove(<Railcraft:ingot:3>);
NEI.hide(<Railcraft:nugget:*>);
NEI.hide(<Railcraft:ingot:*>);

NEI.hide(<Railcraft:fluid.creosote.refactory>);
NEI.hide(<Railcraft:fluid.steam.bottle>);


recipes.remove(<Railcraft:part.circuit:0>);
recipes.addShaped(<Railcraft:part.circuit:0>, 
	[[],
	[null, <hbm:item.circuit>, null], 
	[<hbm:tile.radio_torch_sender>, <hbm:item.circuit:3>, <hbm:tile.radio_torch_receiver>]]);

recipes.remove(<Railcraft:part.circuit:1>);
recipes.addShaped(<Railcraft:part.circuit:1>, 
	[[],
	[null, <hbm:item.circuit>],
	[<hbm:tile.radio_torch_receiver>, <hbm:item.circuit:3>]]);

recipes.remove(<Railcraft:part.circuit:2>);
recipes.addShaped(<Railcraft:part.circuit:2>, 
	[[],
	[null, <hbm:item.circuit>],
	[<hbm:tile.radio_torch_sender>, <hbm:item.circuit:3>]]);

recipes.remove(<Railcraft:part.rail:5>);
recipes.addShaped(<Railcraft:part.rail:5> * 6, 
	[[<Railcraft:part.rail>, <ore:ingotCopper>, <Railcraft:part.rail>], 
	[<Railcraft:part.rail>, <ore:ingotCopper>, <Railcraft:part.rail>], 
	[<Railcraft:part.rail>, <ore:ingotCopper>, <Railcraft:part.rail>]]);

recipes.remove(<Railcraft:part.rail:3>);
recipes.addShaped(<Railcraft:part.rail:3> * 12, 
	[[<ore:ingotSteel>, <ore:StainlessSteel>, <ore:ingotGold>], 
	[<ore:ingotSteel>, <ore:StainlessSteel>, <ore:ingotGold>], 
	[<ore:ingotSteel>, <ore:StainlessSteel>, <ore:ingotGold>]]);

recipes.remove(<Railcraft:part.rail:4>);
recipes.addShaped(<Railcraft:part.rail:4> * 12, 
	[[<ore:ingotSteel>, null, <ore:ingotSteel>], 
	[<ore:ingotSteel>, <hbm:item.ingot_dura_steel>, <ore:ingotSteel>], 
	[<ore:ingotSteel>, null, <ore:ingotSteel>]]);

recipes.remove(<Railcraft:part.rail>);
recipes.addShaped(<Railcraft:part.rail> * 12, 
	[[<ore:ingotIron>, null, <ore:ingotIron>], 
	[<ore:ingotIron>, null, <ore:ingotIron>], 
	[<ore:ingotIron>, null, <ore:ingotIron>]]);
	
recipes.addShaped(<Railcraft:part.tie>, 
	[[], 
	[], 
	[<ore:slabWood>, <ore:slabWood>, <ore:slabWood>]]);
	
recipes.addShaped(<Railcraft:part.rail> * 24, 
	[[<ore:ingotSteel>, null, <ore:ingotSteel>], 
	[<ore:ingotSteel>, null, <ore:ingotSteel>], 
	[<ore:ingotSteel>, null, <ore:ingotSteel>]]);
	
recipes.remove(<Railcraft:part.rebar>);
recipes.addShaped(<Railcraft:part.rebar> * 8, 
	[[null, null, <minecraft:iron_ingot>], 
	[null, <minecraft:iron_ingot>, null], 
	[<minecraft:iron_ingot>, null, null]]);
recipes.addShaped(<Railcraft:part.rebar> * 16, 
	[[null, null, <ore:ingotSteel>], 
	[null, <ore:ingotSteel>, null], 
	[<ore:ingotSteel>, null, null]]);

	
#
#-------------Carriages-------------
#



recipes.addShaped(<Railcraft:cart.tank>, 
	[[<ore:blockGlass>], 
	[<minecraft:minecart>], 
	[]]);
	
recipes.remove(<Railcraft:cart.loco.electric>.withTag({model: "railcraft:default"}));
recipes.addShaped(<Railcraft:cart.loco.electric>.withTag({model: "railcraft:default"}), 
	[[<minecraft:redstone_lamp>, <ore:blockSteel>, null], 
	[<ore:blockSteel>, <hbm:tile.machine_converter_he_rf>, <ore:blockSteel>], 
	[<hbm:item.turbine_titanium>, <minecraft:minecart>, <hbm:item.turbine_titanium>]]);
	
recipes.remove(<Railcraft:cart.loco.steam.solid>.withTag({model: "railcraft:default"}));
recipes.addShaped(<Railcraft:cart.loco.steam.solid>.withTag({model: "railcraft:default"}), 
	[[<ore:blockSteel>, <ore:blockSteel>, <hbm:tile.heater_firebox>], 
	[<ore:blockSteel>, <ore:blockSteel>, <hbm:tile.heater_firebox>], 
	[<ore:barsIron>, <minecraft:minecart>, <minecraft:minecart>]]);




	
#
#-------------Tools-------------
#

recipes.remove(<Railcraft:tool.electric.meter>);
recipes.addShaped(<Railcraft:tool.electric.meter>, 
	[[<ore:ingotAluminum>, null, <ore:ingotAluminum>], 
	[<ore:buttonStone>, <ore:paneGlass>, <ore:buttonStone>], 
	[null, <ore:ingotCopper>, null]]);

recipes.remove(<Railcraft:tool.crowbar>);
recipes.addShaped(<Railcraft:tool.crowbar>, 
	[[null, <ore:ingotAnyRubber>, <ore:ingotIron>], 
	[<ore:ingotAnyRubber>, <ore:ingotIron>, <ore:ingotAnyRubber>], 
	[<ore:ingotIron>, <ore:ingotAnyRubber>, null]]);

recipes.remove(<Railcraft:tool.crowbar.reinforced>);
recipes.addShaped(<Railcraft:tool.crowbar.reinforced>, 
	[[null, <ore:Rubber>, <ore:ingotSteel>], 
	[<ore:Rubber>, <ore:ingotSteel>, <ore:Rubber>], 
	[<ore:ingotSteel>, <ore:Rubber>, null]]);

#
#-------------Machines-------------
#

recipes.remove(<Railcraft:machine.epsilon:3>);
recipes.addShaped(<Railcraft:machine.epsilon:3>, 
	[[<ore:plateAluminum>, <ore:ingotCopper>, <ore:plateAluminum>], 
	[<ore:ingotCopper>, <ore:blockDiamond>, <ore:ingotCopper>], 
	[<ore:plateAluminum>, <ore:ingotCopper>, <ore:plateAluminum>]]);
	
recipes.remove(<Railcraft:machine.epsilon:4>);
recipes.addShaped(<Railcraft:machine.epsilon:4>, 
	[[<ore:plateCopper>, <ore:ingotGold>, <ore:plateCopper>], 
	[<ore:ingotGold>, <ore:blockRedstone>, <ore:ingotGold>], 
	[<ore:plateCopper>, <ore:ingotGold>, <ore:plateCopper>]]);
	
recipes.remove(<Railcraft:signal:2>);
recipes.addShaped(<Railcraft:signal:2> * 2, 
	[[],
	[<hbm:tile.steel_beam>, <hbm:item.part_generic>, <hbm:tile.radio_torch_receiver>], 
	[<hbm:item.plate_steel>, <ore:plateSteel>, <ore:plateSteel>]]);

recipes.remove(<Railcraft:signal:4>);
recipes.addShaped(<Railcraft:signal:4> * 2, 
	[[],
	[<hbm:tile.steel_beam>, <minecraft:lever>, <hbm:item.plate_steel>], 
	[<ore:plateSteel>, <ore:plateSteel>, <ore:plateSteel>]]);

recipes.remove(<Railcraft:detector:12>);
recipes.addShaped(<Railcraft:detector:12>, 
	[[<hbm:item.ingot_firebrick>, <hbm:item.ingot_firebrick>, <hbm:item.ingot_firebrick>], 
	[<hbm:item.ingot_firebrick>, <minecraft:stone_pressure_plate:*>, <hbm:item.ingot_firebrick>], 
	[<hbm:item.ingot_firebrick>, <hbm:item.ingot_firebrick>, <hbm:item.ingot_firebrick>]]);

recipes.remove(<Railcraft:detector:16>);
recipes.addShaped(<Railcraft:detector:16>, 
	[[<minecraft:quartz>, <minecraft:quartz>, <minecraft:quartz>], 
	[<minecraft:quartz>, <minecraft:stone_pressure_plate:*>, <minecraft:quartz>], 
	[<minecraft:quartz>, <minecraft:quartz>, <minecraft:quartz>]]);

recipes.remove(<Railcraft:machine.gamma:2>);
recipes.addShaped(<Railcraft:machine.gamma:2>, 
	[[<ore:ingotSteel>, <ore:dustRedstone>, <ore:ingotSteel>], 
	[<ore:dustRedstone>, <Railcraft:machine.gamma>, <ore:dustRedstone>], 
	[<ore:ingotSteel>, <hbm:item.circuit:7>, <ore:ingotSteel>]]);
	
recipes.remove(<Railcraft:machine.gamma:3>);
recipes.addShaped(<Railcraft:machine.gamma:3>, 
	[[<ore:ingotSteel>, <ore:dustRedstone>, <ore:ingotSteel>], 
	[<ore:dustRedstone>, <Railcraft:machine.gamma:1>, <ore:dustRedstone>], 
	[<ore:ingotSteel>, <hbm:item.circuit:7>, <ore:ingotSteel>]]);

recipes.remove(<Railcraft:machine.delta>);
recipes.addShaped(<Railcraft:machine.delta>, 
	[[null, <hbm:item.plate_polymer>, null], 
	[<hbm:item.plate_polymer>, <hbm:tile.red_cable>, <hbm:item.plate_polymer>], 
	[null, <hbm:item.plate_polymer>, null]]);

recipes.remove(<Railcraft:post:5>);
recipes.addShaped(<Railcraft:post:5>, [[null, <minecraft:stone_slab:5>, null], [null, <Railcraft:post:1>, null]]);

recipes.remove(<Railcraft:post:6>);
recipes.addShaped(<Railcraft:post:6> * 2, [[null, <hbm:item.plate_iron>, null], [null, <Railcraft:post:2>, null]]);
recipes.addShaped(<Railcraft:post:6> * 4, [[null, <hbm:item.plate_steel>, null], [null, <Railcraft:post:2>, null]]);

#
#-------------Decoration-------------
#

recipes.remove(<Railcraft:glass>);
NEI.hide(<Railcraft:glass:*>);

furnace.remove(<Railcraft:brick.bleachedbone:2>);
recipes.addShapeless(<Railcraft:brick.bleachedbone:5> * 32, [<ore:dyeWhite>, <ore:dyeWhite>, <ore:dyeWhite>, 
	<ore:dyeWhite>, <minecraft:clay_ball>, <ore:dyeWhite>,
	<ore:dyeWhite>, <ore:dyeWhite>, <ore:dyeWhite>]);

recipes.removeShaped(<Railcraft:brick.frostbound:2>, 
	[[<minecraft:ice>, <minecraft:ice>, <minecraft:ice>], 
	[<minecraft:ice>, <ore:gemLapis>, <minecraft:ice>], 
	[<minecraft:ice>, <minecraft:ice>, <minecraft:ice>]]);
recipes.addShaped(<Railcraft:brick.frostbound:5> * 32, 
	[[<minecraft:ice>, <minecraft:ice>, <minecraft:ice>], 
	[<minecraft:ice>, <ore:dyeBlue>, <minecraft:ice>], 
	[<minecraft:ice>, <minecraft:ice>, <minecraft:ice>]]);

recipes.addShapeless(<Railcraft:brick.quarried:5> * 32, [<chisel:marble>, <minecraft:cobblestone>, <chisel:marble>, 
	<minecraft:cobblestone>, <minecraft:cobblestone>, <minecraft:cobblestone>,
	<chisel:marble>, <minecraft:cobblestone>, <chisel:marble>]);
	

recipes.removeShapeless(<Railcraft:brick.bloodstained:2>, [<minecraft:sandstone:2>, <minecraft:rotten_flesh>]);
recipes.removeShapeless(<Railcraft:brick.bloodstained:2>, [<minecraft:sandstone:2>, <minecraft:beef>]);

recipes.addShapeless(<Railcraft:brick.bloodstained:5> * 32, 
	[<minecraft:cobblestone>, <minecraft:cobblestone>, <minecraft:cobblestone>,
	<minecraft:cobblestone>, <minecraft:rotten_flesh>, <minecraft:cobblestone>,
	<minecraft:cobblestone>, <minecraft:cobblestone>, <minecraft:cobblestone>]);
	
recipes.addShapeless(<Railcraft:brick.abyssal:5> * 32, 
	[<minecraft:cobblestone>, <minecraft:cobblestone>, <minecraft:cobblestone>,
	<minecraft:cobblestone>, <ore:anyTar>, <minecraft:cobblestone>,
	<minecraft:cobblestone>, <minecraft:cobblestone>, <minecraft:cobblestone>]);
	
recipes.removeShaped(<Railcraft:brick.sandy:2>, [[<ore:ingotBrick>, <minecraft:sand>], [<minecraft:sand>, <ore:ingotBrick>]]);
recipes.addShapeless(<Railcraft:brick.sandy:5>, 
	[<minecraft:brick>, <minecraft:brick>, <minecraft:brick>,
	<minecraft:brick>, <minecraft:sand>, <minecraft:sand>,
	<minecraft:sand>, <minecraft:sand>]);










	
	

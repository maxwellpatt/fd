import csv

players = "95766-84669:Luka Doncic 95766-49111:Joel Embiid 95766-55062:Nikola Jokic 95766-15755:Anthony Davis 95766-84680:Shai Gilgeous-Alexander 95766-80808:Jayson Tatum 95766-40199:Giannis Antetokounmpo 95766-9488:LeBron James 95766-59358:Domantas Sabonis 95766-145337:Tyrese Haliburton 95766-9524:Stephen Curry 95766-80810:De'Aaron Fox 95766-9644:James Harden 95766-84671:Trae Young 95766-145321:Anthony Edwards 95766-14498:Kyrie Irving 95766-20848:Damian Lillard 95766-145331:Tyrese Maxey 95766-12341:Paul George 95766-188414:Victor Wembanyama 95766-14528:Jimmy Butler 95766-80817:Bam Adebayo 95766-67708:Dejounte Murray 95766-63122:Kristaps Porzingis 95766-80812:Lauri Markkanen 95766-58462:Karl-Anthony Towns 95766-14513:Kawhi Leonard 95766-84690:Jalen Brunson 95766-157908:Alperen Sengun 95766-66048:Brandon Ingram 95766-24247:Fred VanVleet 95766-110312:Tyler Herro 95766-157808:Cade Cunningham 95766-110310:Zion Williamson 95766-171759:Chet Holmgren 95766-14514:Nikola Vucevic 95766-19067:CJ McCollum 95766-171770:Paolo Banchero 95766-67026:Jaylen Brown 95766-42669:Julius Randle 95766-58377:Kyle Kuzma 95766-157905:Josh Giddey 95766-40203:Rudy Gobert 95766-66108:Jamal Murray 95766-84670:Mikal Bridges 95766-58253:Myles Turner 95766-9642:Russell Westbrook 95766-9714:DeMar DeRozan 95766-171779:Jalen Duren 95766-110347:Keldon Johnson 95766-40783:Zach LaVine 95766-157851:Franz Wagner 95766-66115:Ben Simmons 95766-14518:Tobias Harris 95766-157838:Cam Thomas 95766-9663:Jrue Holiday 95766-171760:Jalen Williams 95766-110354:Nic Claxton 95766-9623:Chris Paul 95766-58312:D'Angelo Russell 95766-14503:Jonas Valanciunas 95766-110322:Jordan Poole 95766-145324:Devin Vassell 95766-188426:Ausar Thompson 95766-15542:Spencer Dinwiddie 95766-80815:Zach Collins 95766-157907:Jalen Green 95766-171787:Keegan Murray 95766-15860:Draymond Green 95766-66236:John Collins 95766-84682:Michael Porter 95766-20640:Jordan Clarkson 95766-84709:Mitchell Robinson 95766-171767:Jabari Smith 95766-110357:RJ Barrett 95766-157833:Jalen Johnson 95766-171749:Jeremy Sochan 95766-55059:Clint Capela 95766-58153:Kelly Oubre 95766-158136:Austin Reaves 95766-41594:Aaron Gordon 95766-58081:Tyus Jones 95766-110337:Talen Horton-Tucker 95766-145304:Onyeka Okongwu 95766-145539:Deni Avdija 95766-157850:Jalen Suggs 95766-9621:Brook Lopez 95766-16261:Khris Middleton 95766-157848:Herbert Jones 95766-49675:Derrick White 95766-171777:Walker Kessler 95766-110338:De'Andre Hunter 95766-80805:Markelle Fultz 95766-145327:Cole Anthony 95766-70827:Ivica Zubac 95766-110316:Cameron Johnson 95766-60233:Dillon Brooks 95766-145323:Tre Jones 95766-188425:Dereck Lively 95766-23716:Kyle Anderson 95766-111273:Luguentz Dort 95766-145307:Isaiah Stewart 95766-145348:Immanuel Quickley 95766-110995:Naz Reid 95766-15846:Tim Hardaway 95766-80816:Malik Monk 95766-145489:Killian Hayes 95766-42156:Bobby Portis 95766-14509:Klay Thompson 95766-84704:Kevin Huerter 95766-110325:Daniel Gafford 95766-23665:Buddy Hield 95766-157812:Davion Mitchell 95766-58576:Kevon Looney 95766-9575:Mike Conley 95766-84694:Bruce Brown 95766-110318:Grant Williams 95766-42202:Christian Wood 95766-15946:Harrison Barnes 95766-84703:De'Anthony Melton 95766-16293:Norman Powell 95766-40562:Josh Hart 95766-171746:Bennedict Mathurin 95766-84714:Moritz Wagner 95766-145328:Saddiq Bey 95766-16376:Dorian Finney-Smith 95766-84679:Marvin Bagley 95766-110326:Coby White 95766-55060:Bogdan Bogdanovic 95766-49116:Andrew Wiggins 95766-188427:Marcus Sasser 95766-14510:Alec Burks 95766-9453:Al Horford 95766-18338:Royce O'Neale 95766-145319:Jaden McDaniels 95766-9535:Kyle Lowry 95766-9874:Kevin Love 95766-84702:Lonnie Walker 95766-110359:Goga Bitadze 95766-40830:Delon Wright 95766-15590:Mason Plumlee 95766-171748:Malaki Branham 95766-145333:Aaron Nesmith 95766-188408:Anthony Black 95766-171747:Andrew Nembhard 95766-171780:Jaden Ivey 95766-55056:Dario Saric 95766-18393:T.J. McConnell 95766-22541:Kelly Olynyk 95766-157839:Day'Ron Sharpe 95766-15636:Kentavious Caldwell-Pope 95766-66064:Malik Beasley 95766-171744:Christian Braun 95766-110315:Terance Mann 95766-145322:Jalen Smith 95766-145325:Josh Green 95766-188416:Bilal Coulibaly 95766-23572:Taurean Prince 95766-15557:Andre Drummond 95766-157904:Jonathan Kuminga 95766-23981:Alex Caruso 95766-171784:Dyson Daniels 95766-80825:Isaiah Hartenstein 95766-157819:Corey Kispert 95766-66968:Derrick Jones 95766-113267:Caleb Martin 95766-158373:Jose Alvarado 95766-84681:Donte DiVincenzo 95766-67312:Thomas Bryant 95766-16233:Josh Richardson 95766-145339:Obi Toppin 95766-188421:Jordan Hawkins 95766-20491:Robert Covington 95766-157827:Isaiah Jackson 95766-158854:Sam Hauser 95766-14523:Reggie Jackson 95766-84667:Collin Sexton 95766-145308:Patrick Williams 95766-80811:Jonathan Isaac 95766-188415:Cason Wallace 95766-58461:Trey Lyles 95766-157834:Bones Hyland 95766-85137:Duncan Robinson 95766-15800:Jae Crowder 95766-171665:Orlando Robinson 95766-171769:Tari Eason 95766-110339:Cam Reddish 95766-145329:Paul Reed 95766-188422:Jaime Jaquez 95766-157802:Moses Moody 95766-58519:Gary Payton 95766-145576:Jae'Sean Tate 95766-12474:Patrick Beverley 95766-9637:Danilo Gallinari 95766-20992:Larry Nance 95766-9809:Nicolas Batum 95766-162411:Matt Ryan 95766-63126:Cedi Osman 95766-84724:Landry Shamet 95766-145305:Zeke Nnaji 95766-80814:Dennis Smith 95766-145335:Payton Pritchard 95766-145533:Kenyon Martin 95766-158856:Trendon Watford 95766-14512:Marcus Morris 95766-48567:Cameron Payne 95766-158137:Jock Landale 95766-15993:Pat Connaughton 95766-102025:Haywood Highsmith 95766-84691:Shake Milton 95766-81621:Maxi Kleber 95766-84696:Jevon Carter 95766-171761:Peyton Watson 95766-110356:Nickeil Alexander-Walker 95766-20277:Torrey Craig 95766-111492:Amir Coffey 95766-145330:Isaiah Joe 95766-24544:Gary Harris 95766-188405:Amen Thompson 95766-188412:Keyonte George 95766-188418:Kobe Brown 95766-188445:Jordan Miller 95766-188450:Trayce Jackson-Davis 95766-157805:Brandon Boston 95766-41083:Luke Kornet 95766-157826:Quentin Grimes 95766-157828:Chris Duarte 95766-157829:Aaron Wiggins 95766-157849:Ayo Dosunmu 95766-23802:Kris Dunn 95766-17894:Mike Muscala 95766-117291:Armoni Brooks 95766-171752:AJ Griffin 95766-171758:Jaylin Williams 95766-171766:Johnny Davis 95766-171781:Ochai Agbaji 95766-110349:Rui Hachimura 95766-171791:Jaden Hardy 95766-171792:Nikola Jovic 95766-161553:Dru Smith 95766-80829:Sasha Vezenkov 95766-159702:Eugene Omoruyi 95766-188433:Brandin Podziemski 95766-145538:Aleksej Pokusevski 95766-157831:Tre Mann 95766-157842:Charles Bassey 95766-157840:Jaden Springer 95766-70826:Furkan Korkmaz 95766-15583:Seth Curry 95766-15684:Victor Oladipo 95766-180555:Jamal Cain 95766-15691:Cody Zeller 95766-9739:JaVale McGee 95766-173747:Simone Fontecchio 95766-84668:Troy Brown 95766-110336:Chuma Okeke 95766-171795:Ousmane Dieng 95766-16196:Dwight Powell 95766-23407:P.J. Tucker 95766-145313:Jordan Nwora 95766-188409:Jarace Walker 95766-188423:Julian Strawther 95766-188448:Colby Jones 95766-188452:Leonard Miller 95766-157821:Dalano Banton 95766-160963:Daishen Nix 95766-85305:Kenrich Williams 95766-9648:Jeff Green 95766-163280:Olivier Sarr 95766-117283:Oshae Brissett 95766-15947:Reggie Bullock 95766-85597:Jordan McLaughlin 95766-84706:Devonte' Graham 95766-171751:Max Christie 95766-171772:Ryan Rollins 95766-23294:Danuel House 95766-110340:Jaxson Hayes 95766-55055:Dante Exum 95766-171802:MarJon Beauchamp 95766-18256:Doug McDermott 95766-145316:Kira Lewis 95766-59318:Joe Ingles 95766-145347:James Wiseman 95766-145351:Omer Yurtseven 95766-16363:Joe Harris 95766-188410:Ben Sheppard 95766-188411:Taylor Hendricks 95766-188417:Kobe Bufkin 95766-111622:Garrison Mathews 95766-188424:Olivier-Maxence Prosper 95766-101387:Gabe Vincent 95766-188430:Dariq Whitehead 95766-188431:Noah Clowney 95766-189456:Malcolm Cazalon 95766-188432:Jalen Hood-Schifino 95766-188442:Jalen Wilson 95766-188446:Sidy Cissoko 95766-189468:Colin Castleton 95766-189469:D'Moi Hodge 95766-189475:Miles Norris 95766-188449:Jalen Slawson 95766-188454:Mouhamed Gueye 95766-188455:Seth Lundy 95766-188453:Jaylen Clark 95766-188458:Jalen Pickett 95766-188459:Hunter Tyson 95766-188457:Jordan Walsh 95766-188463:Julian Phillips 95766-188460:Isaiah Wong 95766-190515:Onuralp Bitim 95766-117808:Marques Bolden 95766-110640:Luka Samanic 95766-188464:Andre Jackson 95766-188465:Chris Livingston 95766-188470:Terquavion Smith 95766-188471:Ricky Council 95766-188468:Keyontae Johnson 95766-188469:Maxwell Lewis 95766-188474:Jacob Toppin 95766-188475:Oscar Tshiebwe 95766-188478:Sir'Jabari Rice 95766-172098:Julian Champagnie 95766-188480:Adama Sanogo 95766-145490:Trevelin Queen 95766-145491:Nathan Knight 95766-157803:Josh Christopher 95766-157801:Jared Butler 95766-157807:Luka Garza 95766-157804:Keon Johnson 95766-157810:Isaiah Livers 95766-157811:Neemias Queta 95766-157813:Joshua Primo 95766-157823:Greg Brown 95766-157824:Miles McBride 95766-157825:Jericho Sims 95766-157830:Jeremiah Robinson-Earl 95766-145541:R.J. Hampton 95766-157835:Kessler Edwards 95766-145548:Anthony Gill 95766-157841:Filip Petrusev 95766-157846:Sandro Mamukelashvili 95766-157847:Trey Murphy 95766-116906:Lindell Wigginton 95766-14511:Markieff Morris 95766-23740:Ryan Arcidiacono 95766-14529:Cory Joseph 95766-14530:Bojan Bogdanovic 95766-164036:Braxton Key 95766-14543:Davis Bertans 95766-157906:Usman Garuba 95766-16604:Justin Holiday 95766-195815:Charles Bediako 95766-180484:Stanley Umude 95766-180485:John Butler 95766-160022:A.J. Lawson 95766-145738:Nate Hinton 95766-63826:Boban Marjanovic 95766-9561:DeAndre Jordan 95766-159097:Jay Huff 95766-145819:Naji Marshall 95766-145822:Kevon Harris 95766-145824:Jordan Ford 95766-193991:Alex Fudge 95766-15814:Alex Len 95766-40396:Monte Morris 95766-180737:Jeenathan Williams 95766-117285:Vlatko Cancar 95766-175653:Jared Rhoden 95766-117290:Charlie Brown 95766-23096:Evan Fournier 95766-117307:DaQuan Jeffries 95766-180793:Jermaine Samuels 95766-9799:Wesley Matthews 95766-81529:Daniel Theis 95766-171658:Johnny Juzang 95766-171659:Lester Quinones 95766-9873:Robin Lopez 95766-171670:Dereon Seabron 95766-171668:Collin Gillespie 95766-171669:Keon Ellis 95766-171672:A.J. Green 95766-171673:Justin Lewis 95766-158371:Terry Taylor 95766-171680:Cole Swider 95766-84675:Mo Bamba 95766-84677:Jerome Robinson 95766-84676:Wendell Carter 95766-9939:Patty Mills 95766-171745:Kendall Brown 95766-171750:Blake Wesley 95766-84713:Svi Mykhailiuk 95766-84719:Aaron Holiday 95766-171762:JD Davison 95766-84721:Jarred Vanderbilt 95766-171763:Dalen Terry 95766-171765:Moussa Diabate 95766-110329:Bruno Fernando 95766-171771:Caleb Houstan 95766-110328:Admiral Schofield 95766-171768:TyTy Washington 95766-171773:Patrick Baldwin 95766-171778:Wendell Moore 95766-171776:Josh Minott 95766-110341:Dylan Windler 95766-171783:E.J. Liddell 95766-161551:Javonte Smart 95766-111372:Thanasis Antetokounmpo 95766-161552:Micah Potter 95766-55065:Vasilije Micic 95766-192339:Dexter Dennis 95766-171925:Dominick Barlow 95766-23447:Richaun Holmes 95766-80806:Lonzo Ball 95766-80819:Harry Giles 95766-145352:Trent Forrest 95766-145357:Lamar Stevens 95766-165854:Lindy Waters 95766-188406:Cam Whitmore 95766-188407:Jett Howard 95766-188413:Brice Sensabaugh"

# Split the string into a list where each element is one player's info
players_list = players.split('\n')

# Prepare data for CSV
csv_data = []

# Add a header row with enough columns
header_row = ['Player {}'.format(i+1) for i in range(len(players_list))]
csv_data.append(header_row)

# Prepare a row for the players
player_row = []

for player in players_list:
    # Remove the first 13 characters (up to and including the colon)
    full_name = player[13:]
    # Add the full name to the player row
    player_row.append(full_name)

# Add the player row to the csv data
csv_data.append(player_row)

# Write the data to a CSV file
with open('players3.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

print("CSV file 'players3.csv' has been created and saved.")




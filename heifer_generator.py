from cow import Cow

class HeiferGenerator:

	cows = None

	cowNames = ['heifer', 'kitteh', 'dave', 'aHiddenCow', 'anotherHiddenCow']

	quoteLines = '    \\\n' 
	quoteLines += '     \\\n'
	quoteLines += '      \\\n'

	cowImages = [	"        ^__^\n" +
					"        (oo)\\_______\n" +
					"        (__)\\       )\\/\\\n" +
					"            ||----w |\n" +
					"            ||     ||\n",


					"       (\"`-'  '-/\") .___..--' ' \"`-._\n" +
					"         ` *_ *  )    `-.   (      ) .`-.__. `)\n" +
					"         (_Y_.) ' ._   )   `._` ;  `` -. .-'\n" +
					"      _.. `--'_..-_/   /--' _ .' ,4\n" +
					"   ( i l ),-''  ( l i),'  ( ( ! .-'\n",
											
											
					"                 ,#####,\n" +                        
					"                 #_   _#\n" +
					"                 |a` `a|\n" +                       
					"                 |  u  |\n" +
					"                 \\  =  /\n" +
					"                 |\\___/|\n" +
					"        ___ ____/:     :\\____ ___\n" +
					"      .'   `.-===-\\   /-===-.`   '.\n" +
					"     /      .-\"\"\"\"\"-.-\"\"\"\"\"-.      \\\n" +
					"    /'             =:=             '\\\n" +
					"  .'  ' .:    o   -=:=-   o    :. '  `.\n" +
					"  (.'   /'. '-.....-'-.....-' .'\\   '.)\n" +
					"  /' ._/   \".     --:--     .\"   \\_. '\\\n" + 
					" |  .'|      \".  ---:---  .\"      |'.  |\n" +
					" |  : |       |  ---:---  |       | :  |\n" +
					"  \\ : |       |_____._____|       | : /\n" +
					"  /   (       |----|------|       )   \\\n" +
					" /... .|      |    |      |      |. ...\\\n" +
					"|::::/''     /     |       \\     ''\\::::|\n" +
					"'\"\"\"\"       /'    .L_      `\\       \"\"\"\"'\n" +
					"           /'-.,__/` `\\__..-'\\\n" +
					"          ;      /     \\      ;\n" +
					"          :     /       \\     |\n" +
					"          |    /         \\.   |\n" +
					"          |`../           |  ,/\n" +
					"          ( _ )           |  _)\n" +
					"          |   |           |   |\n" +
					"          |___|           \\___|\n" +
					"          :===|            |==|\n" +
					"           \\  /            |__|\n" +
					"           /\\/\\           /\"\"\"8.__\n" +
					"           |oo|           \\__.//___)\n" +
					"           |==|\n" +
					"           \\__/\n",
					
					"secretImage1",

					"secretImage2"
				]

	def get_cows():
		if HeiferGenerator.cows is None:
			HeiferGenerator.cows = [None]*len(HeiferGenerator.cowImages)
			for index in range(len(HeiferGenerator.cows)):
				HeiferGenerator.cows[index] = Cow(HeiferGenerator.cowNames[index])
				HeiferGenerator.cows[index].set_image(HeiferGenerator.quoteLines + HeiferGenerator.cowImages[index])
		
		return HeiferGenerator.cows

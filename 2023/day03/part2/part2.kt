import java.io.File
import java.io.InputStream


val numbers = listOf("0", "1", "2", "3", "4", "5", "6", "7", "8", "9");
var quicknDirty: Int = 0;


//Because we are multiplying now if gear only has 2, it is changed to ar eutrn value of 1, so 0 doesnt reset us to 0 constantly.
fun numberBuild(lineList: MutableList<String>, i:Int, j:Int) : Int
{
	if (i < 0 || i > lineList.size - 1 || j < 0 || j > lineList[i].length - 1)
		return (1);
	if (!(lineList[i][j].toString() in numbers))
		return (1);
	var startOfString: Int = j;
	while (startOfString > 0)
	{
		startOfString--;
		if (!(lineList[i][startOfString].toString() in numbers))
		{
			startOfString++;
			break;
		}
	}
	var endOfString = j;
	while (endOfString < lineList[i].length - 1)
	{
		endOfString++;
		if (!(lineList[i][endOfString].toString() in numbers))
		{
			endOfString--;
			break;
		}
	}
	// println(startOfString)
	// println(endOfString);
	// println(lineList[i].substring(startOfString, endOfString - startOfString));
	quicknDirty++;
	return (lineList[i].substring(startOfString, endOfString + 1).toInt());
}

fun searchAround(lineList: MutableList<String>, i:Int , j: Int) : Int
{
	//Checking numbers above
	var toAdd: Int = 1;
	quicknDirty = 0;
	//Checking if uppermiddle is a number, if it is dont need to check left and top right
	if (i > 0)
	{
		if (lineList[i - 1][j].toString() in numbers)
			toAdd *= numberBuild(lineList, i - 1, j);
		else
		{
			toAdd *= numberBuild(lineList, i - 1, j - 1);
			toAdd *= numberBuild(lineList, i - 1, j + 1);	
		}
	}
	//Adding Top Left Number and Top Right Number (This only if top middle is not a digit)
	//Adding Both Side Numbers
	toAdd *= numberBuild(lineList, i, j - 1);
	toAdd *= numberBuild(lineList, i, j + 1);
	//Checking the bottom middle, same as the top number situation
	if (i < lineList.size - 1)
	{
		if (lineList[i + 1][j].toString() in numbers)
			toAdd *= numberBuild(lineList, i + 1, j);
		else
		{
			toAdd *= numberBuild(lineList, i + 1, j - 1);
			toAdd *= numberBuild(lineList, i + 1, j + 1);
		}
	}
	if (quicknDirty == 2)
		return (toAdd);
	return (0);
}

fun main()
{
	val inputStream: InputStream = File("input.txt").inputStream();
	var lineList = mutableListOf<String>();
	var total: Int = 0;

	inputStream.bufferedReader().forEachLine { lineList.add(it) };
	for(i in 0..lineList.size - 1)
	{
		for (j in 0..lineList[i].length - 1)
		{
			if (lineList[i][j].toString() == "*")
			{
				total += searchAround(lineList, i, j);
			}
		}
	}
	println(total)
}
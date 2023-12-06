import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Vector;
import java.io.*;
import javax.management.Descriptor;

import java.util.ArrayList;
import java.util.Collections;
import java.util.*;
import java.util.HashMap; // import the HashMap class

/*
* Day 6:
* marker is defined as a window string of at least length4 where all chars are unique
* sliding i window of size 4 and check that len(set(wind)) == len(window)
* return i + 4
 */


class Read {

	public static void main(String[] args) {
		String filepath = "input.txt";

		try{
			File file = new File(filepath);

			// Creating an object of BufferedReader class
			BufferedReader br = new BufferedReader(new FileReader(file));

			// Declaring a string variable
			String st;
			List<String> input = new ArrayList<>();

			while ((st = br.readLine()) != null)
 
            // Print the string
            input.add(st);

			String signal = input.get(0);
			int ans =  -1;

			for (int i = 0; i <= signal.length()-14; i++){
				String window =  signal.substring(i, i+14);
				//convert window to hashset
				Set<Character> set = new LinkedHashSet<>();
				window.chars().forEach(e -> set.add((char) e));
				if (set.size() == 14){
					ans = i;
					break;
				}
			}

			System.out.println(ans+14);
		}
		catch(IOException ie) {
			ie.printStackTrace();
		}   
 	}

}
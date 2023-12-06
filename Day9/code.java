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
* Day 9:
* HT and both initally at 0,0 (doesn't matter really where they start) as long as we have a starting point
* for every move H, T needs to catch up to it
* if H and T are in same row or column, T will move up 1 in that direction to stat close to it
* Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up:
* return the number of positions where T has touched at least once

* simulate and dump (i,j) into seen set whenver T moves
* maintin variables for positions of T and H
* apply moves to H, and whenver T needs to catch up, update its poisition accordingly
* every time we move to, add it position to a seen set

*/


class Read {

    public static void ApplyMove(Integer[] starting_H, String move){
		//move head
		if (move.equals("U")){
			starting_H[1] += 1;
		}
		else if (move.equals("D")){
			starting_H[1] -= 1;
		}

		else if (move.equals("L")){
			starting_H[0] -= 1;
		}

		else if (move.equals("R")){
			starting_H[0] += 1;
		}

    }

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
            Integer[] starting_T = {0,0};
            Integer[] starting_H = {0,0};

			for (String line: input){
				//split line 
				String[] line_split = line.split(" ");
				String dirr = line_split[0];
				String size = line_split[1];
				Integer int_size = Integer.parseInt(size);
				ApplyMove(starting_H, dirr);
				System.out.println(starting_H[0]);
			}


            



            

		}
		catch(IOException ie) {
			ie.printStackTrace();
		}   
 	}

}
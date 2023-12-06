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
* Day 8:
part 1
* given a list of 2d intergers, where each ineteger represents the height of a tree
* count the number of visible trees from the edge
* motonic stack from in all four directions
* id of each tree is going to its (i,j) position, dumpy into hashset
* then just return the size of the hashset

part 2
* we want to find the highest scenic score possible
* for each tree, look at all cardnal directions and multiply its viewing distance
* we define viewing distance as the furthers tree we can such that the last tree we can see in that direction is at most this current tree's height

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
            
            //get the dimensions
            Integer rows = input.size();
            Integer cols = input.get(0).length();

            //edge trees
            Integer edge_trees = (rows*4) - 4;
            Integer inner_trees = 0;

            //hahset for seen trees, key will cell number, retreive by "i$j" indices
            HashSet<String> seen_trees = new HashSet<>();
            boolean[][] seen = new boolean[rows][cols];

            //check looking down from first row
            for (int col = 1; col < cols-1; col++){
                Integer curr_max = Character.getNumericValue(input.get(0).charAt(col));
                for (int row = 1; row < rows - 1; row++){
                    char curr_char = input.get(row).charAt(col);
                    //convert to int
                    Integer curr_char_int = Character.getNumericValue(curr_char);
                    //if bigger than curr max and not seen yet
                    if (curr_char_int > curr_max){
                        curr_max = curr_char_int;
                        if (seen[row][col] == false){
                            inner_trees += 1;
                            seen[row][col] = true;
                        }
                    }
                }
            }

            //check looking left
            for (int row = 1; row < rows-1; row++){
                Integer curr_max = Character.getNumericValue(input.get(row).charAt(0));
                for (int col = 1; col < cols - 1; col++){
                    char curr_char = input.get(row).charAt(col);
                    //convert to int
                    Integer curr_char_int = Character.getNumericValue(curr_char);
                    //if bigger than curr max and not seen yet
                    if (curr_char_int > curr_max){
                        curr_max = curr_char_int;
                        if (seen[row][col] == false){
                            inner_trees += 1;
                            seen[row][col] = true;
                        }
                    }
                }
            }

        
            //looking up from bottom
            for (int col = 1; col < cols-1; col++){
                Integer curr_max = Character.getNumericValue(input.get(rows-1).charAt(col));
                for (int row = rows-2; row > 0; row--){
                    char curr_char = input.get(row).charAt(col);
                    //convert to int
                    Integer curr_char_int = Character.getNumericValue(curr_char);
                    //if bigger than curr max and not seen yet
                    if (curr_char_int > curr_max){
                        curr_max = curr_char_int;
                        if (seen[row][col] == false){
                            inner_trees += 1;
                            seen[row][col] = true;
                        }
                    }
                }
            }

            //looking right to left
            for (int row = 1; row < rows-1; row++){
                Integer curr_max = Character.getNumericValue(input.get(row).charAt(cols-1));
                for (int col = cols-2; col > 0; col--){
                    char curr_char = input.get(row).charAt(col);
                    //convert to int
                    Integer curr_char_int = Character.getNumericValue(curr_char);
                    //if bigger than curr max and not seen yet
                    if (curr_char_int > curr_max){
                        curr_max = curr_char_int;
                        if (seen[row][col] == false){
                            inner_trees += 1;
                            seen[row][col] = true;
                        }
                    }
                }
            }

            //System.out.println(inner_trees+edge_trees);
            //part 2
            /*
             * brute force would be to check all directions for all trees
             * but is there a faster way to get a sceneic score
             * if dp(i,j) represents the sceneic score for tree at i,j
             * then dp(i,j) = {
                up = 1 + dp(i-1,j) if trees[i][j] > trees[i-1][j]
                down = 1 + dp(i+1,j) if trees[i][j] > trees[i-1][j]
            }
             */


            



            

		}
		catch(IOException ie) {
			ie.printStackTrace();
		}   
 	}

}
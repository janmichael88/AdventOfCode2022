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
* Day 7:
* we are givne a list of shell commands and we want to find the file sizes for all the directories
* initiallt through about using recursion but we can iterate this
* just maintain a list for all the paths created so far 
* if it stats with cd
    check if we go back to /
    check if we up up, pop last visited diretor
    otherwise add new path
*if its a file size, add this size to the current directory
* we can just ignor the dir lines anyway


* for part 2
total diskspace available on the file system is 70_000_000
to run the update, you need at least unsesed space of 30_000_000

need to find a directory that can de deleted such that it will free up enough space
out target space would be 70_000_000 minus the size of the directory
we want the smallest size directory that is just gretaer than 30_000_000 - (70_000_000 - size of directory)
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

            HashMap<String,Integer> dirs_to_size = new HashMap<>();
            LinkedList<String> path = new LinkedList<>();
            
            for (String l : input){
                //cd always means we access an unvisited directory
                //if this weren't the case we'd have to walk through the whole tree
                if (l.startsWith("$ cd")){
                    String[] d = l.split(" ");
                    String curr_dir = d[2];

                    if (curr_dir.equals("/")){
                        //add to path
                        path.addLast("/");
                        System.out.print(curr_dir);
                    }
                    //if we go up, we can remove it
                    else if (curr_dir.equals("..")){
                        path.removeLast();
                    }
                    //otherwise this is a first visit for the director
                    else{
                        String new_path = "";
                        if (path.isEmpty() == false){
                        new_path += path.getLast();
                        if (path.getLast().equals("/") == false){
                            new_path += "/";
                        }
                        else{
                            new_path += "";
                        }
                    }
                        new_path += curr_dir;
                        System.out.print(new_path);
                        System.out.print("\n");
                        path.addLast(new_path);
                    } 
                }
                if (Character.isDigit(l.charAt(0))){
                    for (String p:path){
                        Integer curr_size = dirs_to_size.getOrDefault(p, 0);
                        //get curr size of file
                        Integer curr_file_size = Integer.parseInt(l.split(" ")[0]);
                        curr_size += curr_file_size;
                        dirs_to_size.put(p, curr_file_size);
                        
                    }
                }

            }

            //find directories whos sizes are less than 100,000
            Integer less_than = 0;
            for (Integer s : dirs_to_size.values()){
                if (s <= 100_000){
                    less_than += s;
                }
            }
            System.out.println(less_than);
		}
		catch(IOException ie) {
			ie.printStackTrace();
		}   
 	}

}
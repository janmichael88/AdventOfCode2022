import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Vector;

import javax.management.Descriptor;

import java.util.ArrayList;
import java.util.Collections;
import java.util.*;
import java.util.HashMap; // import the HashMap class

/*
* Day 4:
* we are given intervals, we want to count the intervals that completley overlap one another
* for part 2, if moves is 1, we can just move a crate
* otherwise we move all m crates and put them in order
 */


class ReadFileLineByLineUsingBufferedReader {

	public static List<Object> GetInputs(String pathToFile){
		List<Object> ans = new ArrayList<>();
		BufferedReader reader;

		//i first need to build the boxes, boxes is going to be an array
		List<String> boxes = new ArrayList<>();

		//need hashmap to store index in string to box number
		HashMap<Integer,Character> box_to_index = new HashMap<Integer,Character>();

		try {
			reader = new BufferedReader(new FileReader(pathToFile));
			String line = reader.readLine();

			//process boxes input first
			while (line.length() != 0) {
				boxes.add(line);
				line = reader.readLine();
			}
			//get indices for boxes
			String box_idxs = boxes.get(boxes.size()-1);
			for (int i = 0; i < box_idxs.length(); i++){
				char box_num = box_idxs.charAt(i);
				if (box_num != ' '){
					box_to_index.put(i,box_num);
				}
			}

			//container to hold boxes with crates, list of lists
			List<List<Character>> box_with_crates = new ArrayList<>();
			for (int i = 0; i < 9; i++){
				box_with_crates.add(new ArrayList<Character>());
			}
			//for the first N-1 boxes
			for (int i = 0; i < boxes.size() - 1; i++){
				String curr_box = boxes.get(i);
				for (int j = 0; j < curr_box.length(); j++){
					char curr_char = curr_box.charAt(j);
					if ((box_to_index.containsKey(j)) && (curr_char != ' ')){
						//get index of box
						int index_of_box = Character.getNumericValue(box_to_index.get(j));
						//add char to box
						box_with_crates.get(index_of_box-1).add(curr_char);
					}
				}
			}

			//advance and start getting moves
			List<List<Integer>> moves = new ArrayList<>();

			line = reader.readLine();
			while (line != null){
				String[] split_line = line.split(" ");
				//numbers at indices 1,3,5
				
				int amount = Integer.parseInt(split_line[1]);
				int FROM = Integer.parseInt(split_line[3]);
				int TO = Integer.parseInt(split_line[5]);

				List<Integer> curr_move = Arrays.asList(amount,FROM,TO);
				moves.add(curr_move);

				line = reader.readLine();
			}

			reader.close();

			//add to inputs
			ans.add(box_with_crates);
			ans.add(moves);
		} catch (IOException e) {
			e.printStackTrace();
		}
		return ans;
	}
	
	public static void MakeMove(LinkedList<Character> from, LinkedList<Character> to, Integer moves){
		if (moves == 1){
			while (moves > 0){
				moves -= 1;
				char curr = from.getFirst();
				from.removeFirst();
				to.addFirst(curr);

		}
	
		}
		
		else{
			LinkedList<Character> temp = new LinkedList<>();
			while (moves > 0){
				moves -= 1;
				char curr = from.getFirst();
				from.removeFirst();
				temp.addFirst(curr);

			};
			while (temp.size() > 0){
				char curr = temp.getFirst();
				temp.removeFirst();
				to.addFirst(curr);
			}
		}


	}

	public static void main(String[] args) {
		String filpath = "input.txt";
		List<Object> inputs = GetInputs(filpath);

		List<List<Character>> boxes = (List<List<Character>>) inputs.get(0);
		List<List<Integer>> moves = (List<List<Integer>>) inputs.get(1);

		//for the boxes reversed and put them into a list of stacks
		//java is not pass by reference
		//convert boxes to list of stacks
		List<LinkedList> boxes_as_LL = new ArrayList<>();
		for (List<Character> foo : boxes){
			LinkedList<Character> curr = new LinkedList<>(foo);
			boxes_as_LL.add(curr);
		}

		//test function


		//do for all moves
		for (List<Integer> m : moves){
			int num_moves = m.get(0);
			int from_idx = m.get(1);
			int to_idx = m.get(2);

			LinkedList<Character> from_bucket = boxes_as_LL.get(from_idx-1);
			LinkedList<Character> to_bucket = boxes_as_LL.get(to_idx-1);
			MakeMove(from_bucket, to_bucket, num_moves);
		}

		for (LinkedList b : boxes_as_LL){
			System.out.print(b.getFirst());
		}
		System.out.println("\n");

		


	}

}
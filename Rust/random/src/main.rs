use std::io;    // Standard Input Output crate
use rand::Rng;  // Random Number Generator crate

fn main() {
    println!("Guess my secret number it\'s between 1 and 1000!");
    println!("How fast can you guess my number?");

    let secret_number = rand::thread_rng().gen_range(1, 1001); // A random number between 1 and 1000

    println!("The secret number is: {}", secret_number);
}

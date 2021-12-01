use std::fs::File;
use std::path::Path;
use std::io::{self, BufRead};

fn main() {
    let mut lastval:i32 = 0;
    let mut inc_count = 0;
    if let Ok(lines) = read_lines("01.txt") {
        for line in lines {
            if let Ok(val) = line {
                let integer:i32 = val.parse::<i32>().unwrap();
                if lastval < integer && lastval != 0 {
                    inc_count += 1;
                }
                lastval = integer;
                println!("Line:{} {}", val, lastval);
            }
        }
    }
    println!("{}", inc_count.to_string());
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
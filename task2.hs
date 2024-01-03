import System.Environment

subtract1 :: [Int] -> [Int]
subtract1 [] = []
subtract1 (x:xs) = [subtract x 255] ++ subtract1 xs


main :: IO ()
 -- Writing a main I/O function
main = do
    args <- getArgs               -- Command line args are collected as a string

    -- Command line args are collected as a string
    -- read is an inbuilt function to convert string to int. ::[Int] is the type signature
    let numbers = map read args :: [Int]

    -- Call the function
        result = subtract1 numbers

     -- Convert the result back to string
        resultStrings = map show result
        outputString = unwords resultStrings

     -- print the string
    putStrLn outputString

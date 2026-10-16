# Pair Retrospective: test_utils library

- Pair members: Aiden and Kevin
- Repository / branch / PR link: https://github.com/aford277/qe-test-utils-aiden-kevin
- Date and total time spent: October 16th, 2 Hours

## 1. Role-swap log

Fill one row per 30-minute block (add rows if you swapped more often).

| Block | Minutes | Driver | Navigator | What we built | Last commit hash (short) |
|---|---|---|---|---|---|
| 1 | 0-30 | Kevin | Aiden | Everything in Milestone 1 | ba6a4a9 |
| 2 | 30-60 | Aiden | Kevin | Everything in Milestone 2 | f97ab20 |
| 3 | 60-90 | Kevin | Aiden | The first four functions in Milestone 3 | bc59acd |
| 4 | 90-120 | Aiden | Kevin | The rest of Milestone 3 and Milestone 4 | 1fb30e1 |
| 5 | 120-150 | Kevin | Aiden | Milestone 5 | 263b9d6 |

## 2. What went well in how we worked together?
We were both able to help each other complete the code when one was navigating. For example, the navigator helped the driver figure out how seeds worked with random.

## 3. What was difficult?
- Technically: Finishing the demo report, we had a test case that was failing because of an extra space in the formatter. We were stuck on that for a bit.
- As a team (communication, pace, disagreement, git hand-offs): We had some issues with the navigator not properly communicating to the driver what they wanted them to do. 

## 4. What did each of us learn from the other?
- Aiden learned from Kevin: Better tips on how to debug
- Kevin learned from Aiden: How rng and random works in Python

## 5. Our code
- The function we are proudest of, and why: generate_test_cases because it all came together and felt like completing a large portion that took time.
- The function that most needs improvement, and how: The demo report had a format we didn't really like, we would rather the columns be lined up
- One bug we hit and how we found it (error message, what we tried, the fix): We had a bug that caused an infinite loop. We needed to add a randint with a new seed so that we didn't generate the same username over and over again.

## 6. Git collaboration
- Did every swap follow commit, push, pull? What went wrong when we skipped a step? We didn't skip any steps
- Did we get a merge conflict? How did we resolve it (or why not)? We did not get a merge conflict because the code we each wrote did not overlap each others work
- Output of `git shortlog -sne` (paste): 
8  Aiden Ford <aford277@hotmail.com>
6  Kevin Nguyen <kevintrongkhangnguyen@gmail.com>

## 7. Next time
- Two things we would do differently: Better planning when doing each function. Researching new libraries before implementing them.
- Self-rating, 1 (poor) to 5 (excellent): communication 4, keeping to the swap timer 5, understanding every line 4.5

## 8. Final check
Paste the last lines of `python3 check_exercise.py` (the "x/y checks passed" line): 
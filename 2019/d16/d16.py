#!/usr/bin/env python3

class Day16:

  def getPattern(self, pos, totlen):
    base_pattern = [0, 1, 0, -1]
    pattern = [x for x in base_pattern for i in range(pos)]
    pattern2 = pattern[1:] + [pattern[0]]

    if totlen > len(pattern2):
      pattern2 = pattern2 * ((totlen // len(pattern2)) + 1)
    
    return pattern2[:totlen]
    
  def partA(self, inputsignal):
    res = []
    for i in range(len(inputsignal)):
      pattern = self.getPattern(i+1, len(inputsignal))
      sum_numbers = abs(sum(map(lambda x,y: x * y, pattern, inputsignal)))
      res.append(sum_numbers if sum_numbers < 10 else sum_numbers % 10)
    
    return res


if __name__ == '__main__':
  inputsignal = [int(x) for x in '59755896917240436883590128801944128314960209697748772345812613779993681653921392130717892227131006192013685880745266526841332344702777305618883690373009336723473576156891364433286347884341961199051928996407043083548530093856815242033836083385939123450194798886212218010265373470007419214532232070451413688761272161702869979111131739824016812416524959294631126604590525290614379571194343492489744116326306020911208862544356883420805148475867290136336455908593094711599372850605375386612760951870928631855149794159903638892258493374678363533942710253713596745816693277358122032544598918296670821584532099850685820371134731741105889842092969953797293495']
  d = Day16()
  for i in range(100):
    inputsignal = d.partA(inputsignal)
  print(inputsignal[:8])
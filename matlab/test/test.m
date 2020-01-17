%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%                               test                              %%%%%
%%%%%                            Raul Tapia                           %%%%%
%%%%%      GRVC Robotics Laboratory at the University of Seville      %%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% @file    test.m
% @brief   Test for parseOptitrackCSV function.
% @author  Raul Tapia

addpath('../src');

rb = parseOptitrackCSV('test.csv');

figure();
plot(rb.t, rb.position);
xlabel('t');
ylabel('position');
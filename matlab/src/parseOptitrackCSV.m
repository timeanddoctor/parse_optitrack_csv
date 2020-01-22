%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%                        parseOptitrackCSV                        %%%%%
%%%%%                            Raul Tapia                           %%%%%
%%%%%      GRVC Robotics Laboratory at the University of Seville      %%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% @file    parseOptitrackCSV.m
% @brief   Parse exported csv files from Motive software.
% @author  Raul Tapia

% @param   filename   Name of the csv file
% @return  rigidBody  Structure with data
function rigidBody = parseOptitrackCSV(filename)
    %%% Load data
    data = importdata(filename);

    %%% Rigid body
    rigidBody.frame           = data.data(:,1);
    rigidBody.t               = data.data(:,2);
    rigidBody.quaternion      = data.data(:,3:6);
    rigidBody.position        = data.data(:,7:9);
    rigidBody.meanMarkerError = data.data(:,10);

    %%% Check number of markers
    numMarkers = char(data.textdata(3));
    numMarkers = str2double(numMarkers(end));

    %%% Markers
    for k = 1:numMarkers
        rigidBody.marker(k).position = data.data(:,(11+(k-1)*4):(13+(k-1)*4));
        rigidBody.marker(k).quality  = data.data(:,14+(k-1)*4);
    end

    %%% Check errors
    rigidBody.framesWithError = rigidBody.frame(isnan(rigidBody.position(:,1)));
end

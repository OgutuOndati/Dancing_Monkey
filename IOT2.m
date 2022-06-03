dataField1 = randi(10, 10, 1);
dataField2 = randi(10, 10, 1);
    % Generate timestamps for the data
tStamps = [datetime('now')-minutes(9):minutes(1):datetime('now')]';
 
    % Create table
dataTable = table(tStamps, dataField1, dataField2);
channelID = 1757733;
writeKey  = 'DAHGT5W891L9Y72M';
thingSpeakWrite(channelID, dataTable, 'WriteKey', writeKey)
disp('process completed')
function SoilViewer(boring_data)

    % Set the resolution for the interpolation/plotting
    dx = 10;
    x = boring_data(1,1):dx:boring_data(1,end);
    % run the spline, surpressing any warnings
    warning('off','all');
    data = mySoilSpline(boring_data,x);
    warning('on','all');
    % convert from depths to elevations
    data(3:end,:)=repmat(data(2,:),size(data,1)-2,1)-data(3:end,:);
    % Remove the NaN by copying data from the next row (fixs fill error)
    data(isnan(data)) = data(find(isnan(data))+1);
    
    % Extract the water table data from the dataset
    water_table = data(3,:);
    % Extract soil layer data from the dataset
    soil_layers = [data(2,:); data(4:end,:)];
    % Extraxt boring shafts from data
    bore_loc = repmat(boring_data(1,:),2,1);
    bore_ele = [boring_data(2,:); boring_data(2,:)-boring_data(end,:)];
    
    % Create a new figure to plot in
    figure;
    hold on;
    % plot handles
    h = NaN(1,size(soil_layers,1)+2);
    % Plot soil layers
    c = autumn(size(soil_layers,1)-1);
    for n = 2:size(soil_layers,1)
        h(n) = fill([x,flip(x)],[soil_layers(n,:), flip(soil_layers(n-1,:))],c(n-1,:));
    end
    % Plot water table
    h(end-1) = plot(x, water_table,'b--','Linewidth',2);
    % Plot boring shafts 
    temp = plot(bore_loc, bore_ele,'k','Linewidth',2);
    h(end) = temp(1);
    hold off;
    % Format the plot so it looks nice:
    margin = [50, 50, 25, 5];
    axis([min(x)-margin(1), max(x)+margin(2), min(min(data(2:end,:)))-margin(3), max(max(data(2:end,:)))+margin(4)]);
    legend('Fill','Medium Sand','Silty Clay','Fine Sand with Clay','Water Table','Borehole','Location','southwest');
    title('Soil Profile','FontSize',16);
    xlabel('x-location (m)');
    ylabel('Elevataion (m)');
end
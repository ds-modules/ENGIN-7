function [C] = myAirQualityAnalytic(V, Q, beta, C_vent, t0, C0, ...
    t_start, t_end, E_value, t)

% Calculate analytical solution for C when E is a top-hat function and
% assuming t_start > t0.
%
% Input arguments:
%
% - V, Q, beta, C_vent, t_start, t_end, and E_value: they are the same as
% for the function myAirQuality (see instructions).
%
% - t0 and C0 should be scalars of class double. t0 and C0 specify the
% initial condition. C0 is the particle mass concentration at time t0. In
% other words: C(t0)=C0.
%
% - t should be an array of class double. t specifies the times at which
% the particle mass concentration must be calculated.
%
% Outut argument:
%
% - C is an array of class double which has the same size as t. C(i) is the
% particle mass concentration at time t(i).
%
% Note: the only quality check that this function does on its input
% arguments is to check that t_start > t0. If the input arguments of this
% function are invalid in other aspects, unexpected behavior may occur.

if t_start <= t0
    error('This function assumes that t_start > t0')
end

% Calculate intermediate values
tau = V / (Q + beta*V);
a = Q / V * C_vent * tau;

% f is the analytical solution of the governing equation for C together
% with the initial condition C(t_initial)=C_start, assuming that E is
% constant (but it can be non-zero)
f = @(t_initial, C_start, E, times) a + E/V*tau + ...
    (C_start - a - E/V*tau) * exp(-(times-t_initial) / tau);

% Inialize the output array
C = zeros(size(t));

% Separate the times in three intervals
before = t <= t_start;
after = t > t_end;
middle = ~before & ~after;

% Solution for t <= t_start
C(before) = f(t0, C0, 0, t(before));

% Solution for t_start < t <= t_end
C_t_start = f(t0, C0, 0, t_start);
C(middle) = f(t_start, C_t_start, E_value, t(middle));

% Solution for t > t_end
C_t_end = f(t_start, C_t_start, E_value, t_end);
C(after) = f(t_end, C_t_end, 0, t(after));

end
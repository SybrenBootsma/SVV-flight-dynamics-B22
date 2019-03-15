load('FTISxprt-20190312_101442.mat')

data = flightdata

vane_AOA = flightdata.vane_AOA.data;
elevator_dte = flightdata.elevator_dte.data ;
column_fe = flightdata.column_fe.data ;
lh_engine_FMF = flightdata.lh_engine_FMF.data ;
rh_engine_FMF = flightdata.rh_engine_FMF.data ;
lh_engine_itt = flightdata.lh_engine_itt.data ;
rh_engine_itt = flightdata.rh_engine_itt.data ;
lh_engine_OP = flightdata.lh_engine_OP.data ;
rh_engine_OP = flightdata.rh_engine_OP.data ;
lh_engine_fan_N1 = flightdata.lh_engine_fan_N1.data ;
lh_engine_turbine_N2 = flightdata.lh_engine_turbine_N2.data ;
rh_engine_fan_N1 = flightdata.rh_engine_fan_N1.data ;
rh_engine_turbine_N2 = flightdata.rh_engine_turbine_N2.data ;
lh_engine_FU = flightdata.lh_engine_FU.data ; 
rh_engine_FU = flightdata.rh_engine_FU.data ;
delta_a = flightdata.delta_a.data ;
delta_e = flightdata.delta_e.data ;
delta_r = flightdata.delta_r.data ;
GPS_date = flightdata.Gps_date.data ;
GPS_utcSec = flightdata.Gps_utcSec.data ;
Ahrs1_Roll = flightdata.Ahrs1_Roll.data ;
Ahrs1_Pitch = flightdata.Ahrs1_Pitch.data ;
Fms1_trueHeading = flightdata.Fms1_trueHeading.data ;
Gps_lat = flightdata.Gps_lat.data ;
Gps_long = flightdata.Gps_long.data ;
Ahrs1_bRollRate = flightdata.Ahrs1_bRollRate.data ;
Ahrs1_bPitchRate = flightdata.Ahrs1_bPitchRate.data ;
Ahrs1_bYawRate = flightdata.Ahrs1_bYawRate.data ;
Ahrs1_bLongAcc = flightdata.Ahrs1_bLongAcc.data ;
Ahrs1_bLatAcc = flightdata.Ahrs1_bLatAcc.data ;
Ahrs1_bNormAcc = flightdata.Ahrs1_bNormAcc.data ;
Ahrs1_aHdgAcc = flightdata.Ahrs1_aHdgAcc.data ;
Ahrs1_xHdgAcc = flightdata.Ahrs1_xHdgAcc.data ;
Ahrs1_VertAcc = flightdata.Ahrs1_VertAcc.data ;
Dadc1_sat = flightdata.Dadc1_sat.data ;
Dadc1_tat = flightdata.Dadc1_tat.data ;
Dadc1_alt = flightdata.Dadc1_alt.data ;
Dadc1_bcAlt = flightdata.Dadc1_bcAlt.data ;
Dadc1_bcAltMb = flightdata.Dadc1_bcAltMb.data ;
Dadc1_mach = flightdata.Dadc1_mach.data ;
Dadc1_cas = flightdata.Dadc1_cas.data ;
Dadc1_tas = flightdata.Dadc1_tas.data ;
Dadc1_altRate = flightdata.Dadc1_altRate.data ;
measurement_running = flightdata.measurement_running.data ;
measurement_n_rdy = flightdata.measurement_n_rdy.data ;
display_graph_state = flightdata.display_graph_state.data ;
display_active_screen = flightdata.display_active_screen.data ;
time = flightdata.time.data ;
time = transpose(time) ;

csvwrite('vane_AOA.csv', vane_AOA)
csvwrite('elevator_dte.csv', elevator_dte)
csvwrite('column_fe.csv', column_fe)
csvwrite('lh_engine_FMF.csv', lh_engine_FMF)
csvwrite('rh_engine_FMF.csv', rh_engine_FMF)
csvwrite('lh_engine_itt.csv', lh_engine_itt)
csvwrite('rh_engine_itt.csv', rh_engine_itt)
csvwrite('lh_engine_OP.csv', lh_engine_OP)
csvwrite('rh_engine_OP.csv', rh_engine_OP)
csvwrite('lh_engine_fan_N1.csv', lh_engine_fan_N1)
csvwrite('lh_engine_turbine_N2.csv', lh_engine_turbine_N2)
csvwrite('rh_engine_fan_N1.csv', rh_engine_fan_N1)
csvwrite('rh_engine_turbine_N2.csv', rh_engine_turbine_N2)
csvwrite('lh_engine_FU.csv', lh_engine_FU)
csvwrite('rh_engine_FU.csv', rh_engine_FU)
csvwrite('delta_a.csv', delta_a)
csvwrite('delta_e.csv', delta_e)
csvwrite('delta_r.csv', delta_r)
csvwrite('GPS_date.csv', GPS_date)
csvwrite('GPS_utcSec.csv', GPS_utcSec)
csvwrite('Ahrs1_Roll.csv', Ahrs1_Roll)
csvwrite('Ahrs1_Pitch.csv', Ahrs1_Pitch)
csvwrite('Fms1_trueHeading.csv', Fms1_trueHeading)
csvwrite('Gps_lat.csv', Gps_lat)
csvwrite('Gps_long.csv', Gps_long)
csvwrite('Ahrs1_bRollRate.csv', Ahrs1_bRollRate)
csvwrite('Ahrs1_bPitchRate.csv', Ahrs1_bPitchRate)
csvwrite('Ahrs1_bYawRate.csv', Ahrs1_bYawRate)
csvwrite('Ahrs1_bLongAcc.csv', Ahrs1_bLongAcc)
csvwrite('Ahrs1_bLatAcc.csv', Ahrs1_bLatAcc)
csvwrite('Ahrs1_bNormAcc.csv', Ahrs1_bNormAcc)
csvwrite('Ahrs1_aHdgAcc.csv', Ahrs1_aHdgAcc)
csvwrite('Ahrs1_xHdgAcc.csv', Ahrs1_xHdgAcc)
csvwrite('Ahrs1_VertAcc.csv', Ahrs1_VertAcc)
csvwrite('Dadc1_sat.csv', Dadc1_sat)
csvwrite('Dadc1_tat.csv', Dadc1_tat)
csvwrite('Dadc1_alt.csv', Dadc1_alt)
csvwrite('Dadc1_bcAlt.csv', Dadc1_bcAlt)
csvwrite('Dadc1_bcAltMb.csv', Dadc1_bcAltMb)
csvwrite('Dadc1_mach.csv', Dadc1_mach)
csvwrite('Dadc1_cas.csv', Dadc1_cas)
csvwrite('Dadc1_tas.csv', Dadc1_tas)
csvwrite('Dadc1_altRate.csv', Dadc1_altRate)
csvwrite('measurement_running.csv', measurement_running)
csvwrite('measurement_n_rdy.csv', measurement_n_rdy)
csvwrite('display_graph_state.csv', display_graph_state)
csvwrite('display_active_screen.csv', display_active_screen)
csvwrite('time.csv', time)
load('matlab.mat')

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

csvwrite('GPS_long.csv', Gps_long)
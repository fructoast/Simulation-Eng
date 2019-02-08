#include <stdio.h>
#define N 30
int main(void)
{
  int i,j;
  double part;
  double variable[N] = {};
  double a[N][N+1]={{60.324941,1.374457,0.305730,0.576954,1.692663,0.014339,0.212413,1.895340,1.041172,0.982464,0.064586,1.981785,1.588534,1.522784,0.991616,1.408502,0.798366,1.768859,1.329003,1.895329,1.114736,0.644892,0.694127,1.599785,0.945864,1.238347,1.648942,0.117535,0.968457,0.853431,32.555504},
  {0.860886,54.514093,0.901662,1.437840,1.920551,0.916001,1.650253,1.815890,1.957173,0.632717,1.880476,1.938958,0.221251,1.403261,0.930574,1.629753,0.201627,0.699433,0.958756,0.096956,1.814169,1.603648,0.791083,1.413954,0.549512,0.029429,1.062896,0.667047,0.997886,1.916327,48.968557},
  {1.858772,0.144215,33.183886,1.296612,0.064766,1.080643,0.946864,1.880656,1.037816,1.579581,1.761133,0.976774,1.800833,1.164393,1.907348,1.430586,1.366020,0.606781,0.389342,1.462977,0.420950,1.992990,0.254059,1.834903,0.542501,0.283488,0.897800,1.209549,1.281375,0.814127,20.803989},
  {1.140147,0.958342,0.637171,35.095571,1.023107,1.717814,1.383623,0.903764,0.755630,0.963204,0.664896,1.732404,0.764037,1.829289,1.639752,0.194623,1.195310,0.246533,0.583965,0.658286,0.667482,0.576954,0.912346,0.502386,1.119456,1.195834,1.400185,0.329005,0.477209,0.214312,25.775883},
  {1.617356,1.172654,1.438704,0.054114,46.482549,1.156518,1.437737,1.099525,1.912148,0.400942,1.764421,1.644552,1.164979,1.593710,1.284303,1.359602,0.789020,1.530836,1.943567,1.447306,0.198318,0.520521,0.359652,0.700704,1.639977,1.555486,0.100889,1.968982,0.032695,0.315201,32.577944},
  {1.650051,1.487854,0.209220,1.704165,1.683615,32.562814,1.141902,0.783140,1.277886,1.542844,0.547560,0.922437,0.707823,0.141271,0.206741,0.067426,0.930291,1.737577,0.010993,0.377597,1.935895,0.531514,0.737249,0.636598,0.171491,0.292734,0.737487,0.140473,0.325429,1.052688,24.629870},
  {1.975480,0.540542,1.120208,1.679645,0.224158,0.485946,32.263353,1.007297,1.763831,0.364391,1.554858,0.686269,1.072215,1.696128,0.893009,1.139641,0.626419,0.630586,1.150633,1.004016,0.566480,1.682147,1.741264,1.203079,1.853639,0.033999,1.940566,1.994112,0.359427,0.993254,29.469816},
  {0.334907,1.533797,0.025309,0.014552,1.757954,0.511254,0.836099,27.394318,0.275086,1.200490,0.320109,0.961354,0.272705,0.016238,1.854364,1.412346,0.642657,0.484949,0.562979,1.646672,1.051430,0.245126,1.387937,0.254508,0.098765,1.421935,0.195075,0.092877,1.781363,1.188329,21.468310},
  {0.116270,0.722126,1.023287,0.130821,0.480080,1.534541,0.966920,1.245332,27.053270,0.167410,1.565441,0.770981,0.440115,1.581679,0.625345,1.852460,0.224335,1.110294,0.415439,1.871008,0.161724,0.660565,1.258944,0.416232,0.759331,0.680880,0.611307,0.852208,0.462242,1.799636,34.359594},
  {0.578512,0.521762,0.873473,0.709333,1.001842,0.408014,1.676253,0.247173,0.217641,42.204591,1.812614,0.988622,0.283777,1.394293,1.613967,0.136237,1.618628,0.724261,0.551677,1.489636,0.885985,1.212242,0.748581,1.302217,1.971573,1.429460,1.913524,0.823781,1.891703,1.713160,27.012970},
  {0.470215,0.234922,1.547439,1.179548,1.236764,1.955453,0.855801,1.483937,0.173093,0.699463,49.752591,1.161715,0.983241,0.690845,0.775682,1.119478,0.309473,1.499943,1.671155,1.799109,0.385928,0.883397,0.547690,1.688145,0.854969,1.977151,1.601669,1.678750,1.868853,1.314829,23.061160},
  {0.339068,1.549751,1.900155,1.518616,0.786515,1.855608,0.374417,0.270452,0.028701,1.073880,1.567003,47.673746,0.057121,0.257848,1.966099,1.176599,0.567321,1.466042,0.847754,0.366431,1.851970,1.731150,0.914121,1.540115,0.586120,0.891271,1.141784,0.264870,0.760125,0.456614,25.793502},
  {1.099193,0.006365,0.517741,0.617809,0.792879,0.373349,0.992226,1.063331,0.402050,0.066107,0.630335,1.592466,25.463014,0.888183,1.558565,1.299827,1.455504,1.024607,0.147580,1.821935,0.876577,1.878731,0.736056,0.416692,0.464850,1.627327,1.558476,0.729720,0.387452,0.015090,25.666224},
  {1.486645,0.021454,1.865047,0.104454,0.814333,0.238395,1.096681,1.877665,0.640445,1.162787,0.507999,0.232912,1.286015,53.626733,1.791476,0.585841,0.851686,0.816083,0.733422,0.673621,1.692660,0.612152,1.409676,0.109351,1.077003,1.037003,1.667827,1.806722,1.424455,1.682917,42.902245},
  {0.911100,1.704371,1.019075,1.015555,0.518705,1.257470,0.112235,0.396369,1.897915,1.275023,0.904369,0.130827,0.561037,0.300550,48.209070,1.146879,1.152236,0.738386,1.880300,1.825857,0.431046,0.492452,1.235533,0.540398,1.569455,0.272537,0.208225,1.376178,1.696992,1.891142,25.588339},
  {0.608092,1.595513,1.549280,1.623647,0.114218,0.806750,1.735883,0.510588,0.704666,1.010905,1.414956,0.835493,1.571943,1.715506,0.757796,49.219731,0.867743,1.496183,0.599122,0.693600,1.927229,1.091574,1.929133,0.467626,0.661029,0.201669,0.675851,0.037207,1.898661,0.566993,25.699991},
  {0.506754,0.162507,0.116693,0.130401,0.276725,0.923443,1.866284,0.787313,1.628109,0.877189,0.202269,0.463602,0.449132,1.917775,1.221398,1.167953,33.784377,0.717581,1.767075,1.479117,0.644810,0.858649,1.408250,1.112436,1.519678,1.609920,1.788288,1.556885,1.508581,0.355281,16.278864},
  {0.015335,0.517788,0.240989,0.145735,0.794513,1.164432,0.012019,1.581826,0.792541,0.889208,1.784094,1.256143,1.338339,1.701869,0.477541,0.506292,0.487387,29.241108,0.273367,1.966504,1.839932,1.132015,1.374754,0.952368,0.651693,0.984674,0.740656,0.208578,0.493255,1.095937,15.363536},
  {0.508590,1.613726,0.573864,0.654325,0.408239,1.738297,0.666344,1.990064,0.530838,1.555552,1.774159,1.786981,0.893891,1.476028,0.264522,1.400183,1.963415,1.459645,51.300239,1.929919,1.299577,0.805565,1.304673,0.251945,1.457259,0.289348,0.992601,1.665836,0.782602,0.088539,63.387775},
  {1.291192,1.702264,0.572575,1.945517,0.110503,0.310872,0.611861,0.100568,0.841709,0.167412,1.874726,0.628691,1.061303,1.350754,0.893213,0.461486,1.314169,0.352858,0.135036,46.533487,1.652434,0.940601,0.548761,1.904379,0.397860,0.838109,0.896981,0.063696,1.620711,0.985520,12.591298},
  {0.911903,0.687784,0.634982,0.857420,0.798288,0.945854,1.469281,0.898855,1.787563,1.636693,0.773581,0.416254,0.697997,0.124336,1.309467,1.159483,1.438504,1.662324,1.294519,0.682592,46.287642,0.235121,1.231354,1.219138,0.632981,0.069462,0.116119,0.696677,1.690174,1.101639,29.145196},
  {0.602077,1.789423,1.394066,1.459497,0.587711,0.339920,0.928778,1.486566,0.127483,0.565471,0.260147,0.543737,1.263468,0.384483,1.853204,0.422951,1.822987,1.515529,1.717470,0.505579,0.830287,52.067823,1.736933,0.049426,0.585571,1.806395,0.165545,1.282248,1.496569,1.267184,12.527495},
  {0.098646,1.056607,1.435399,1.558143,1.644318,1.775319,0.486920,1.130884,1.902802,1.052391,1.391031,0.446540,0.315859,1.775514,0.299744,0.738810,1.598501,1.815273,0.456280,0.104081,0.645560,0.408870,44.408580,0.694986,0.994441,1.647409,0.860531,0.276689,1.143978,0.127715,19.404047},
  {1.242623,1.184322,1.753420,0.800766,0.828640,1.528738,1.287686,1.959523,1.431541,0.340078,1.350554,1.878080,0.655937,1.126068,0.177824,1.394747,0.724569,1.993097,1.851026,0.828650,0.638657,0.259896,0.669663,60.050146,1.254337,0.317072,0.194173,1.531026,1.461050,0.321888,68.798363},
  {0.703673,1.506210,1.602467,1.504439,0.334849,1.131206,0.792126,0.294373,0.562746,1.132204,1.644927,0.440827,1.788141,0.770995,0.618651,1.182887,1.495565,0.611747,1.033913,0.324214,1.250404,1.293810,0.993878,0.584046,36.713755,1.310950,0.778220,0.079173,0.772000,1.100107,46.477713},
  {1.475674,0.606317,1.530688,0.980113,0.941166,0.661894,1.772239,1.235539,1.224640,0.904443,0.880466,1.665467,0.692583,1.651461,0.284118,1.875470,1.147026,0.895865,0.909384,1.471240,0.146269,0.203194,0.465118,0.730315,0.751341,47.808390,1.508534,0.830514,0.548068,0.608642,30.619672},
  {0.023742,1.214959,0.289423,1.003855,0.156125,0.951317,0.776094,1.391664,0.175957,1.680536,0.272130,1.841424,0.373119,1.923591,0.125542,0.248590,1.070617,1.021407,1.157974,0.541857,1.167675,1.361167,1.006975,1.897990,0.112508,0.783043,28.460230,0.943022,1.331111,0.015166,34.584861},
  {1.354853,1.230125,1.991180,0.358708,1.386250,0.942497,1.134802,0.777914,1.118454,0.815338,1.050045,0.959879,1.188457,0.973636,1.085420,1.437047,0.044253,0.106827,0.595021,0.586110,1.274502,1.956188,1.593085,1.172492,0.068696,0.376128,0.579016,47.304207,1.707239,0.594182,28.171781},
  {1.062091,1.824307,0.704655,1.420799,1.210558,1.647152,0.555601,1.988472,0.765606,1.370939,1.038517,1.725484,0.559396,0.012153,0.810905,1.996443,0.056405,0.917731,0.591464,0.642515,0.192233,0.547652,0.235600,1.364725,0.616348,0.611728,1.943742,1.628066,54.595542,0.537924,22.522739},
  {1.381058,0.362231,1.046196,0.801857,1.572789,0.693348,1.357458,1.561261,1.458953,0.728396,0.599778,1.184438,1.287792,0.611930,1.995342,1.284235,0.668336,0.913074,1.875699,1.310851,1.105307,0.423351,1.546451,0.470033,1.039699,0.158178,0.413774,0.667765,0.477144,46.995993,36.372951}};

  for(i=0;i<N;i++){
    part = a[i][N];
    for(j=0;j<N-1;j++){
      part -= variable[j]*a[i][j];
    }
    variable[i] = part/a[i][i];

    printf("%2d:  ",i);
    for(j=0;j<N-1;j++){
      printf("%6f",variable[j]);
    }
    printf("\n");
  }


}
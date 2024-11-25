from django.urls import path,include

from rest_framework.routers import DefaultRouter
from .views import *
from sale.SALERestApiviews import SALEViewsets,SALE_AppliViewsets


from .views import *


router=DefaultRouter()
router.register('DSAViewsets',SALEViewsets,basename='dsa-view-sets')
router.register('DSA_Appli_Viewsets',SALE_AppliViewsets,basename='dsa-Appli-view-sets')



urlpatterns = [
    #  path('chat',chat,name='chat'),
     
    path('dsaAllInsurancesCount',dsaAllInsurancesCount,name="dsaAllInsurancesCount"),

    path('dashboard',dsaDashboard,name="dashboard"),

# Apply Loans
    path('saleempapply-business',apply_business,name="empapply-business"),
    path('saleempapplyEducation',apply_Education,name='empapplyEducation'),
    path('saleempapply-home',home_loan,name='empapply-home'),
    path('saleempcreditapply',credit_card,name='empcreditapply'),
    path('saleempapplycar',car_loan,name='empapplyCar'),
    path('saleemplap',lap,name='emplap'),
    path('saleempapply-personal',apply_personal,name='empapply-personal'),
    path('saleempapplyGold',apply_gold,name='empapplyGold'),
    path('saleempapplyotherLoan',apply_otherLoan,name='empapplyotherLoan'),
# Apply Loans

    path('saleindex',dsaIndex,name='dsa-index'),
    path('dsaAll',dsaTotalAllApplications,name="dsa-all"),
    path('busiLoanApi',businessLoanApi,name='busiLoan'),
    path("approved",approvedLoans,name='approved'),
    path('rejected',rejectedLoans,name='rejected-loans'),
    path('showGraph',showAllLoansGraph,name='shoGraph'),
    path("AllLoans",allLOans,name="AllLoans"),
    
    path('jsondatadsa',get_all_dataAsJson,name='jsonDtaa'),
    path('profile',dsaProfile,name='profile'),
    path('alldsaids',getAllDsaIds,name='getAllDsaIds'),
    path('api/totalLoansCount',totalLoansCount,name='totalLoansCount'),
     
    path('api/creditCardCount',creditCardCount,name='creditCardCount'),
    
    
    

     
    #  CheckEligiblity.........
     path('saleempeducheckEligible',educheckEligible,name='educheckEligible'),
     path('saleempbusicheckEligible',busicheckEligible,name='busicheckEligible'),
     path('saleemplapcheckEligible',lapcheckEligible,name='lapcheckEligible'),
     path('saleemphomecheckEligible',homecheckEligible,name='homecheckEligible'),
     path('saleemppersonalcheckEligible',personalcheckEligible,name='personalcheckEligible'),
     path('saleempcarcheckEligible',carcheckEligible,name='carcheckEligible'),
     path('saleempcreditcheckEligible',creditcheckEligible,name='creditcheckEligible'),
     path('saleempgoldcheckEligible',goldcheckEligible,name='goldcheckEligible'),
     path('saleempothercheckEligible',othercheckEligible,name='othercheckEligible'),
     

     
    #  Insurance.........
     path('saleemplifeInsurance',lifeInsurance,name='lifeInsurance'),
     path('saleempgeneralInsurance',generalInsurance,name='generalInsurance'),
     path('saleemphealthInsurance',healthInsurance,name='healthInsurance'),
     path('saleempallInsurance',allInsurance,name='allInsurance'),
     path('totalsale',sale,name='sale'),

    # DSA LOGINS...............
    path('Login',dsaLogin,name='dsalogin'),
    path('Logout',dsaLogout,name='dsalogout'),
    # DSA LOGINS................
   



    path("api/getDsa/<str:register_id>",SALEViewsets.as_view({"get":"getByRegisterId"}),name="get-dsa"),
   





    path("api/",include(router.urls)),
]
